"""C2 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import PartOfSpeech, VocabularyEntry, VocabularySet
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
                    definition=f"{level}阶段专业和批判性讨论中的{topic}词汇。",
                    example=f"我们可以用{word}整合复杂信息。",
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


C2_SETS += _expanded_sets(
    "C2",
    "c2",
    [
        "精确性",
        "对等",
        "批判",
        "反证",
        "公共性",
        "伦理",
        "透明度",
        "正当性",
        "专业性",
        "整合",
        "重构",
        "解释",
        "话语",
    ],
    ["", "词", "表达", "句子", "论证"],
    62,
    31,
)
