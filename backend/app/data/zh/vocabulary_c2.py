"""C2 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import VocabularySet
from app.data.zh.vocabulary_common import build_set

_SPECS_BY_UNIT = {
    "c2-unit-1": [
        ("semantic_precision_c2", "语义精确", "差别"),
        ("advanced_particles_c2", "高级虚词", "语气"),
        ("nuance_c2", "细微差别", "含义"),
    ],
    "c2-unit-2": [
        ("expert_discourse_c2", "专业话语", "术语"),
        ("mediation_c2", "中介表达", "解释"),
        ("specialized_fields_c2", "专业领域", "领域"),
    ],
    "c2-unit-3": [
        ("critical_thinking_c2", "批判思维", "评价"),
        ("assumptions_c2", "前提", "假设"),
        ("counterevidence_c2", "反证", "证据"),
    ],
    "c2-unit-4": [
        ("translation_c2", "翻译", "译文"),
        ("pragmatics_c2", "语用", "意图"),
        ("cross_cultural_c2", "跨文化", "背景"),
    ],
    "c2-unit-5": [
        ("rhetoric_c2", "修辞", "比喻"),
        ("persuasive_writing_c2", "说服性写作", "论点"),
        ("editorial_style_c2", "评论文体", "社论"),
    ],
    "c2-unit-6": [
        ("language_history_c2", "语言历史", "演变"),
        ("loanwords_c2", "外来词", "借词"),
        ("sociolinguistics_c2", "社会语言学", "变体"),
    ],
    "c2-unit-7": [
        ("editing_c2", "编辑", "修改"),
        ("cohesion_c2", "衔接", "过渡"),
        ("professional_revision_c2", "专业改写", "润色"),
    ],
    "c2-unit-8": [("review_c2", "C2复习", "复习")],
}

C2_SETS: list[VocabularySet] = [
    build_set("C2", unit_ref, spec) for unit_ref, specs in _SPECS_BY_UNIT.items() for spec in specs
]
