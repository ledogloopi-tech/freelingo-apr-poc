---
description: "Phase 9 spec — LLM Memory: the AI tutor autonomously remembers important details about the student and injects them into future conversations."
applyTo: "backend/**, frontend/**"
---

# Phase 9 — LLM Memory

## Overview

The AI tutor can silently remember important details about the student (preferences, hobbies, profession, learning goals, struggles, etc.) as they emerge naturally during chat or voice conversations. The LLM appends a structured marker block to its response when it decides something is worth persisting; the backend detects and strips the block before the student ever sees it, then saves the facts to a dedicated `memories` table. Saved memories are injected back into the system prompt for both text chat and voice conversation sessions, giving the tutor persistent cross-session context at zero extra LLM cost (no additional API calls).

Users can view, delete individual, or clear all memories from the Settings page. A brief toast notification appears in both chat and voice when new memories are saved.

---

## Database model

### `memories`

**File:** `backend/app/models/memory.py`

- id — Type: integer; Constraints: PK, autoincrement; Notes: —
- user_id — Type: integer; Constraints: NOT NULL, FK → users(CASCADE), index; Notes: Cascade-deletes with the user
- content — Type: text; Constraints: NOT NULL; Notes: Max 200 chars enforced by service layer
- source — Type: string(10); Constraints: NOT NULL, default `"chat"`; Notes: `"chat"` or `"voice"`
- created_at — Type: datetime; Constraints: NOT NULL, default UTC now (tz-naive); Notes: Used for eviction ordering (oldest first)

**Index:** `ix_memories_user_id` on `user_id`.

---

## Alembic migration

**File:** `backend/alembic/versions/0022_memory.py`  
Revision ID: `0022_memory`, down_revision: `0021_conversation_source`.

Creates the `memories` table with all columns, the FK with CASCADE, and `ix_memories_user_id`. Fully reversible via `downgrade()`.

---

## Memory service

**File:** `backend/app/services/memory_service.py`

### Constants

- `MEMORY_MARKER_RE` — Value: `r"<<MEMORY>>(.*?)<<ENDMEMORY>>"` (DOTALL); Purpose: Detects and removes the LLM-emitted block
- `MAX_MEMORIES_CONTEXT` — Value: 20; Purpose: Maximum memories injected into the system prompt (the most recent)
- `MAX_MEMORY_CHARS` — Value: 200; Purpose: Hard cap on each stored memory item's length
- `MAX_MEMORIES_PER_USER` — Value: 50; Purpose: Hard cap per user; oldest entries are evicted (FIFO) when exceeded

### `MEMORY_SYSTEM_INSTRUCTION`

A multi-line instruction string appended to every system prompt (both chat and voice). It instructs the LLM to:

- Optionally append `<<MEMORY>>{"items":["..."]}<<ENDMEMORY>>` at the very end of a response when it genuinely learns something new about the student.
- Limit each item to 200 characters, in English, self-contained.
- Not repeat already-captured facts.
- Omit the block entirely in most replies (not every response gets a block).

The string uses `{{` / `}}` to escape literal JSON braces so Python's `.format()` call on the composite system prompt correctly converts them to `{` / `}`.

### Functions

- **`parse_memory_marker`** — Signature: `(text: str) → list[str]`. Notes: Extracts items from the marker block; returns `[]` on no match or JSON parse error. Items are stripped and truncated to `MAX_MEMORY_CHARS`.
- **`strip_memory_marker`** — Signature: `(text: str) → str`. Notes: Removes the marker block and trailing whitespace (`MEMORY_MARKER_RE.sub + .rstrip()`).
- **`build_memory_context`** — Signature: `(memories: list[Memory]) → str`. Notes: Formats the most recent `MAX_MEMORIES_CONTEXT` items into a `"Saved memories..."` section for injection into the system prompt. Returns `""` when list is empty.
- **`save_memories`** — Signature: `async (db, user_id, items, source) → int`. Notes: Persists new items; skips exact duplicates (case-sensitive). Evicts oldest entries (FIFO) before inserting when the total would exceed `MAX_MEMORIES_PER_USER`. Commits the session. Returns the count of actually saved items.
- **`get_user_memories`** — Signature: `async (db, user_id) → list[Memory]`. Notes: Returns all memories for a user ordered by `created_at ASC`.
- **`delete_memory`** — Signature: `async (db, memory_id, user_id) → bool`. Notes: Deletes a single memory only if it belongs to `user_id`. Returns `True` on success, `False` if not found or wrong owner.
- **`clear_all_memories`** — Signature: `async (db, user_id) → int`. Notes: Deletes all memories for a user; returns deleted row count.

---

## Chat integration

**File:** `backend/app/routers/chat.py`

### System prompt construction

On every chat request `get_user_memories` is called, the results are passed to `build_memory_context`, and both the memory context and `MEMORY_SYSTEM_INSTRUCTION` are embedded in `TUTOR_SYSTEM_PROMPT` via `.format()`.

### Streaming SSE — marker handling

The SSE generator (`event_stream`) processes tokens from the LLM stream and withholds the memory block from the client:

1. **Detection mid-stream:** when `<<MEMORY>>` is found in the accumulated `full_response`, all text up to that point is yielded to the frontend but no further tokens are forwarded.
2. **Partial prefix protection:** on each token, if `full_response` ends with a partial `<<MEMORY>>` prefix, those characters are held back until the marker is either confirmed or disproved.
3. **Post-stream flush:** after the LLM stream ends, `strip_memory_marker` removes the block; any clean text not yet sent (`len(clean_response) > sent_len`) is yielded.
4. **DB persistence:** the assistant message is saved with `clean_response` (no marker).
5. **Memory persistence:** `parse_memory_marker(full_response)` extracts items; `save_memories` is called (best-effort, with `db.rollback()` on exception).
6. **Signal order:** `{"done": true}` is yielded **after** `save_memories` completes; `{"memory_updated": true}` is yielded immediately after `done` if any items were saved.

### Frontend toast (chat)

**File:** `frontend/src/app/(app)/chat/page.tsx`

- `memoryToast` state (boolean).
- When `data.memory_updated` is received in the SSE loop: `setMemoryToast(true)` + `setTimeout(() => setMemoryToast(false), 3500)`.
- Toast rendered with `animate-in fade-in slide-in-from-top-2` classes; displays `t('memoryUpdated')`.

---

## Voice conversation integration

**File:** `backend/app/services/conversation_pipeline.py`

### System prompt construction

`get_user_memories` is called once in `conversation.py` before the pipeline is instantiated; the result is passed to `ConversationPipeline.__init__` as the `memories` parameter. `build_memory_context` and `MEMORY_SYSTEM_INSTRUCTION` are embedded in `CONVERSATION_SYSTEM_PROMPT` via `.format()` at construction time.

> **Note:** memories saved during a session are not retroactively injected into the same session's system prompt; they become available from the next session onward.

### Pipeline turn — marker handling

During the LLM streaming loop that drives sentence-by-sentence TTS:

1. **Sentence flush:** when `<<MEMORY>>` appears in a buffered sentence, everything before it is sent to TTS and transcript; the marker and everything after is discarded from the TTS path.
2. **Partial prefix protection:** same hold-back logic as in chat.
3. **End-of-stream flush:** `strip_memory_marker(full_response)` produces `clean_full_response`; the `sentence_buffer` is trimmed only when `"<<MEMORY>>" in full_response` (explicit check to avoid a false positive from `.rstrip()` on responses with trailing whitespace).
4. **DB persistence:** assistant message stored as `clean_full_response`.
5. **Memory persistence:** `parse_memory_marker(full_response)` → `save_memories` using a fresh `AsyncSessionLocal` session (best-effort, errors silently ignored).
6. **Signal order:** `{"type": "memory_updated"}` is sent **before** `{"type": "turn_complete"}`.

### Frontend toast (voice)

**File:** `frontend/src/components/conversation/ConversationMode.tsx`

- `memoryToast` state (boolean).
- `case 'memory_updated':` in the WebSocket message switch: `setMemoryToast(true)` + `setTimeout(() => setMemoryToast(false), 3500)`.
- Toast rendered with `animate-in fade-in slide-in-from-top-2` classes; displays `t('memoryUpdated')`.

---

## REST API

**File:** `backend/app/routers/memories.py`  
**Router prefix:** `/api/memories`  
**Tag:** `memories`  
**Auth:** all endpoints require `require_subscription`. Maintenance mode is not applied to these endpoints because memory management is used by text chat and user settings rather than direct LLM service operation.

- GET — Path: `/api/memories`; Rate limit: 30/min; Response: `MemoryListResponse`; Notes: Returns all memories for the current user ordered oldest-first.
- DELETE — Path: `/api/memories/{memory_id}`; Rate limit: 30/min; Response: 204 No Content; Notes: Returns 404 if not found or owned by a different user.
- DELETE — Path: `/api/memories`; Rate limit: 10/min; Response: `ClearAllResponse`; Notes: Deletes all memories; returns `{"deleted": N}`.

### Schemas

```
MemoryOut          { id, content, source, created_at: str (ISO-8601) }
MemoryListResponse { memories: list[MemoryOut] }
ClearAllResponse   { deleted: int }
```

---

## Settings page (frontend)

**File:** `frontend/src/app/(app)/settings/page.tsx`

A **Memory** section is rendered below the legal links:

- On mount, `fetchMemories()` calls `GET /api/memories` and populates a `memories: MItem[]` state array.
- While loading: spinner text (tCommon `loading`).
- When empty: `t('memoryEmpty')` hint text.
- When non-empty: scrollable list (max-h-64) of memory items with per-item `×` delete button (`handleDeleteMemory`) and a **Clear all** button with a `ConfirmDialog` guard (`handleClearAllMemories`).
- Individual deletes are optimistic (local state updated immediately; no reload required).

---

## i18n keys added

Keys added to all 10 locale files (`messages/*.json`):

- `settings` — Key: `sectionMemory`; Purpose: Section header
- `settings` — Key: `memoryEmpty`; Purpose: Empty-state hint
- `settings` — Key: `memoryClearAll`; Purpose: "Clear all" button label
- `settings` — Key: `memoryClearAllTitle`; Purpose: ConfirmDialog title
- `settings` — Key: `memoryClearAllMessage`; Purpose: ConfirmDialog body
- `settings` — Key: `memoryClearAllConfirm`; Purpose: ConfirmDialog confirm button
- `chat` — Key: `memoryUpdated`; Purpose: Toast text in text chat
- `conversation` — Key: `memoryUpdated`; Purpose: Toast text in voice conversation

---

## Configuration

No new environment variables. All limits are hard-coded constants in `memory_service.py` and can be changed there without schema migrations.

- `MAX_MEMORIES_PER_USER` — Default: 50; Effect: FIFO eviction threshold
- `MAX_MEMORIES_CONTEXT` — Default: 20; Effect: Max injected into prompt per request
- `MAX_MEMORY_CHARS` — Default: 200; Effect: Max length per stored item

---

## Tests

**File:** `backend/tests/test_memories.py`

- **`TestParseMemoryMarker`** — single item, multiple items, no marker, invalid JSON, missing `items` key, truncation to 200 chars, multiline marker, empty item filtering
- **`TestStripMemoryMarker`** — removes marker from end, no-op when absent, multiline
- **`TestBuildMemoryContext`** — empty list, formatting, `MAX_MEMORIES_CONTEXT` limiting
- **`test_list_memories_empty`** — GET returns `{"memories": []}`
- **`test_list_memories_with_items`** — GET returns correct content and source
- **`test_delete_memory`** — 204, item gone from DB
- **`test_delete_memory_not_found`** — 404 on unknown id
- **`test_delete_memory_wrong_user`** — 404 when user tries to delete another user's memory (IDOR guard)
- **`test_clear_all_memories`** — 200, count matches, DB empty
- **`test_memories_require_subscription`** — 200 with `STRIPE_ENABLED=false` (self-hosted)
- **`test_memories_blocked_without_stripe_subscription`** — 402 with `STRIPE_ENABLED=true` and no subscription (via `monkeypatch`)
- **`test_save_memories_persists_and_dedupes`** — saves new items, skips exact duplicates
- **`test_get_user_memories_ordered`** — oldest-first ordering
- **`test_delete_memory_service`** — service-layer delete and ownership guard
- **`test_delete_memory_wrong_user_service`** — returns `False` when wrong user_id
- **`test_clear_all_memories_service`** — clears only target user, leaves other users' memories intact
- **`test_chat_strips_memory_marker_from_response`** — marker does not appear in SSE stream body
