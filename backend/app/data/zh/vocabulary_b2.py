"""B2 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import PartOfSpeech, VocabularyEntry, VocabularySet
from app.data.zh.vocabulary_common import build_set

_SPECS_BY_UNIT = {
    "b2-unit-1": [
        ("debate_b2", "讨论辩论", "立场"),
        ("evidence_b2", "证据", "数据"),
        ("society_b2", "社会", "社区"),
    ],
    "b2-unit-2": [
        ("formal_speech_b2", "正式表达", "汇报"),
        ("workplace_b2", "职场", "会议"),
        ("meetings_b2", "会议沟通", "议程"),
    ],
    "b2-unit-3": [
        ("judgement_b2", "判断", "推断"),
        ("news_analysis_b2", "新闻分析", "报道"),
        ("data_trends_b2", "数据趋势", "趋势"),
    ],
    "b2-unit-4": [
        ("cause_effect_b2", "原因和影响", "影响"),
        ("policy_b2", "政策", "措施"),
        ("environment_b2", "环境", "污染"),
    ],
    "b2-unit-5": [
        ("relationships_b2", "复杂关系", "冲突"),
        ("emotions_b2", "情绪", "担心"),
        ("conflict_resolution_b2", "解决冲突", "协商"),
    ],
    "b2-unit-6": [
        ("academic_b2", "学术话题", "概念"),
        ("research_b2", "研究", "调查"),
        ("education_b2", "教育", "课程"),
    ],
    "b2-unit-7": [
        ("media_literacy_b2", "媒体素养", "事实"),
        ("online_discourse_b2", "网络讨论", "评论"),
        ("bias_b2", "偏见", "立场"),
    ],
    "b2-unit-8": [("review_b2", "B2复习", "复习")],
}

B2_SETS: list[VocabularySet] = [
    build_set("B2", unit_ref, spec) for unit_ref, specs in _SPECS_BY_UNIT.items() for spec in specs
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
                    definition=f"{level}阶段分析和论证时使用的{topic}词汇。",
                    example=f"请结合{word}进行分析。",
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


B2_SETS += _expanded_sets(
    "B2",
    "b2",
    [
        "论点",
        "证据",
        "反驳",
        "资料",
        "统计",
        "政策",
        "经济",
        "就业",
        "组织",
        "合同",
        "预算",
        "策略",
        "风险",
        "方案",
    ],
    ["", "词", "表达", "句子", "分析"],
    69,
    35,
)
