"""C1 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import VocabularySet
from app.data.zh.vocabulary_common import build_set

_SPECS_BY_UNIT = {
    "c1-unit-1": [
        ("advanced_argument_c1", "复杂论证", "论证"),
        ("logic_c1", "逻辑", "前提"),
        ("abstract_nouns_c1", "抽象名词", "概念"),
    ],
    "c1-unit-2": [
        ("honorifics_c1", "敬语和客气话", "称呼"),
        ("institutional_interaction_c1", "机构互动", "办理"),
        ("social_hierarchy_c1", "社会关系层级", "身份"),
    ],
    "c1-unit-3": [
        ("academic_reading_c1", "学术阅读", "摘要"),
        ("sources_c1", "资料来源", "出处"),
        ("methodology_c1", "研究方法", "方法"),
    ],
    "c1-unit-4": [
        ("public_discourse_c1", "公共话语", "议题"),
        ("politics_society_c1", "政治和社会", "政策"),
        ("opinion_polling_c1", "民意调查", "样本"),
    ],
    "c1-unit-5": [
        ("style_genre_c1", "文体和体裁", "体裁"),
        ("formal_writing_c1", "正式写作", "段落"),
        ("literary_language_c1", "文学语言", "意象"),
    ],
    "c1-unit-6": [
        ("negotiation_c1", "协商", "条件"),
        ("persuasion_c1", "说服", "理由"),
        ("professional_email_c1", "专业邮件", "回复"),
    ],
    "c1-unit-7": [
        ("literature_c1", "文学", "小说"),
        ("culture_history_c1", "文化和历史", "传统"),
        ("interpretation_c1", "文本解读", "含义"),
    ],
    "c1-unit-8": [("review_c1", "C1复习", "复习")],
}

C1_SETS: list[VocabularySet] = [
    build_set("C1", unit_ref, spec) for unit_ref, specs in _SPECS_BY_UNIT.items() for spec in specs
]
