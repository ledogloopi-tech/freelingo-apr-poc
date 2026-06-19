from __future__ import annotations

import json
import re

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.app_logger import get_logger
from app.models.memory import Memory
from app.services.prompts import common as common_prompts

logger = get_logger(__name__)

MEMORY_SYSTEM_INSTRUCTION_BASE = common_prompts.MEMORY_SYSTEM_INSTRUCTION_BASE
get_memory_system_instruction = common_prompts.get_memory_system_instruction

MEMORY_MARKER_RE = re.compile(r"<<MEMORY>>(.*?)<<ENDMEMORY>>", re.DOTALL)
MAX_MEMORIES_CONTEXT = 20
MAX_MEMORY_CHARS = 200
# Hard cap on stored memories per user. When adding new items would exceed this
# limit, the oldest entries are evicted first (FIFO) to make room. This prevents
# unbounded growth while keeping memories current.
# Only MAX_MEMORIES_CONTEXT (20) are ever injected into the prompt, so 150 gives
# a comfortable buffer across all languages without wasting storage.
MAX_MEMORIES_PER_USER = 150

def parse_memory_marker(text: str) -> list[str]:
    """Extract memory items from a <<MEMORY>>...<<ENDMEMORY>> block.

    Returns a list of item strings (empty list if no marker found or parse error).
    """
    match = MEMORY_MARKER_RE.search(text)
    if not match:
        return []
    try:
        data = json.loads(match.group(1).strip())
        items: list[str] = data.get("items", [])
        return [
            item.strip()[:MAX_MEMORY_CHARS]
            for item in items
            if isinstance(item, str) and item.strip()
        ]
    except json.JSONDecodeError, TypeError, KeyError:
        logger.debug("Failed to parse memory marker JSON")
        return []


def strip_memory_marker(text: str) -> str:
    """Remove the <<MEMORY>>...<<ENDMEMORY>> block from the response text."""
    return MEMORY_MARKER_RE.sub("", text).rstrip()


def build_memory_context(memories: list[Memory]) -> str:
    """Format user memories for injection into the system prompt.

    Returns an empty string if there are no memories.
    """
    if not memories:
        return ""

    items = memories[-MAX_MEMORIES_CONTEXT:]
    lines = "\n".join(f"- {m.content}" for m in items)
    return f"""Saved memories about the student (use these to personalise your responses;
do NOT repeat these facts back to the student unless relevant):
{lines}
"""


async def save_memories(
    db: AsyncSession,
    user_id: int,
    items: list[str],
    source: str = "chat",
    *,
    study_plan_id: int | None = None,
) -> int:
    """Persist new memory items for a user, skipping exact duplicates.

    When adding new items would push the total above MAX_MEMORIES_PER_USER, the
    oldest entries are deleted first (FIFO eviction) to make room, so the cap is
    never exceeded.

    Returns the number of items actually saved.
    """
    if not items:
        return 0

    # Fetch existing memories ordered oldest-first so we can both deduplicate
    # and evict the oldest if needed — a single query does both jobs.
    existing_result = await db.execute(
        select(Memory.id, Memory.content)
        .where(Memory.user_id == user_id)
        .order_by(Memory.created_at.asc())
    )
    existing_rows: list[tuple[int, str]] = existing_result.fetchall()
    existing_ids: list[int] = [r[0] for r in existing_rows]
    existing_contents: set[str] = {r[1] for r in existing_rows}

    new_items = [
        item.strip()[:MAX_MEMORY_CHARS]
        for item in items
        if item.strip()[:MAX_MEMORY_CHARS]
        and item.strip()[:MAX_MEMORY_CHARS] not in existing_contents
    ]

    if not new_items:
        return 0

    # Evict oldest entries if adding new_items would exceed the cap.
    overflow = len(existing_ids) + len(new_items) - MAX_MEMORIES_PER_USER
    if overflow > 0:
        to_evict = existing_ids[:overflow]
        await db.execute(delete(Memory).where(Memory.id.in_(to_evict)))
        logger.info(
            "Evicted %d oldest memories for user %d (cap=%d)",
            len(to_evict),
            user_id,
            MAX_MEMORIES_PER_USER,
        )

    for item in new_items:
        db.add(Memory(user_id=user_id, content=item, source=source, study_plan_id=study_plan_id))

    await db.commit()
    logger.info("Saved %d new memories for user %d", len(new_items), user_id)
    return len(new_items)


async def get_user_memories(
    db: AsyncSession,
    user_id: int,
    *,
    study_plan_id: int | None = None,
) -> list[Memory]:
    """Return all memories for a user, optionally filtered by study plan."""
    query = select(Memory).where(Memory.user_id == user_id)
    if study_plan_id is not None:
        query = query.where(Memory.study_plan_id == study_plan_id)
    result = await db.execute(query.order_by(Memory.created_at.asc()))
    return list(result.scalars().all())


async def delete_memory(db: AsyncSession, memory_id: int, user_id: int) -> bool:
    """Delete a single memory. Returns True if found and deleted."""
    memory = await db.get(Memory, memory_id)
    if memory is None or memory.user_id != user_id:
        return False
    await db.delete(memory)
    await db.commit()
    return True


async def clear_all_memories(
    db: AsyncSession, user_id: int, *, study_plan_id: int | None = None
) -> int:
    """Delete all memories for a user, optionally scoped to a study plan.

    Returns the number deleted.
    """
    stmt = delete(Memory).where(Memory.user_id == user_id)
    if study_plan_id is not None:
        stmt = stmt.where(Memory.study_plan_id == study_plan_id)
    result = await db.execute(stmt)
    await db.commit()
    return result.rowcount or 0
