"""JA curriculum — assembles all CEFR levels."""

from __future__ import annotations

from app.data._types import CEFRLevel, CurriculumUnit, LessonType  # noqa: F401
from app.data.ja.curriculum_a1 import A1_UNITS
from app.data.ja.curriculum_a2 import A2_UNITS
from app.data.ja.curriculum_b1 import B1_UNITS
from app.data.ja.curriculum_b2 import B2_UNITS
from app.data.ja.curriculum_c1 import C1_UNITS
from app.data.ja.curriculum_c2 import C2_UNITS

CEFR_LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]

CURRICULUM: dict[str, list[CurriculumUnit]] = {
    "A1": A1_UNITS,
    "A2": A2_UNITS,
    "B1": B1_UNITS,
    "B2": B2_UNITS,
    "C1": C1_UNITS,
    "C2": C2_UNITS,
}


def get_curriculum_units(level: str) -> list[CurriculumUnit]:
    return CURRICULUM.get(level, [])
