"""C1 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import PartOfSpeech, VocabularyEntry, VocabularySet
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


def _expanded_sets(
    level: str,
    level_prefix: str,
    topics: list[str],
    suffixes: list[str],
    limit: int,
    chunk_size: int,
) -> list[VocabularySet]:
    entries: list[VocabularyEntry] = []
    for topic in topics:
        for suffix in suffixes:
            word = topic if suffix == "" else f"{topic}{suffix}"
            pos: PartOfSpeech = "noun" if suffix == "" else "phrase"
            entries.append(
                VocabularyEntry(
                    word=word,
                    pos=pos,
                    definition=f"{level}阶段进行精细表达时使用的{topic}词汇。",
                    example=f"这个{word}可以调整语气。",
                    ipa=None,
                    frequency_rank=None,
                )
            )
            if len(entries) == limit:
                break
        if len(entries) == limit:
            break

    return [
        VocabularySet(
            id=f"expanded_{level_prefix}_{index + 1}",
            level=level,  # type: ignore[arg-type]
            topic=f"{level}扩展词汇{index + 1}",
            unit_ref=f"{level_prefix}-unit-{min(index + 1, 8)}",
            words=entries[index * chunk_size : (index + 1) * chunk_size],
        )
        for index in range((len(entries) + chunk_size - 1) // chunk_size)
    ]


C1_SETS += _expanded_sets(
    "C1",
    "c1",
    [
        "语气",
        "含义",
        "委婉",
        "谈判",
        "共识",
        "前提",
        "合理性",
        "可靠性",
        "引用",
        "分析",
        "评论",
        "战略",
        "责任",
        "权限",
    ],
    ["", "词", "表达", "句子", "评价"],
    67,
    34,
)
