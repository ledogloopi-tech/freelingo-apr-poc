"""B1 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import PartOfSpeech, VocabularyEntry, VocabularySet
from app.data.zh.vocabulary_common import build_set

_SPECS_BY_UNIT = {
    "b1-unit-1": [
        ("opinions_b1", "观点", "看法"),
        ("arguments_b1", "论据", "理由"),
        ("media_b1", "媒体", "新闻"),
    ],
    "b1-unit-2": [
        ("stories_b1", "故事", "经历"),
        ("life_events_b1", "人生事件", "毕业"),
        ("relationships_b1", "关系", "朋友"),
    ],
    "b1-unit-3": [
        ("advice_b1", "建议", "建议"),
        ("study_work_b1", "学习和工作", "任务"),
        ("wellbeing_b1", "身心状态", "压力"),
    ],
    "b1-unit-4": [
        ("conditions_b1", "条件", "如果"),
        ("plans_problems_b1", "计划和问题", "困难"),
        ("weather_events_b1", "天气事件", "暴雨"),
    ],
    "b1-unit-5": [
        ("politeness_b1", "礼貌", "麻烦"),
        ("requests_refusals_b1", "请求和拒绝", "拒绝"),
        ("customer_service_b1", "客户服务", "客服"),
    ],
    "b1-unit-6": [
        ("culture_b1", "文化", "节日"),
        ("customs_b1", "习俗", "习惯"),
        ("social_life_b1", "社交生活", "聚会"),
    ],
    "b1-unit-7": [
        ("problems_solutions_b1", "问题和解决办法", "办法"),
        ("housing_b1", "住房", "租房"),
        ("technology_support_b1", "技术支持", "维修"),
    ],
    "b1-unit-8": [("review_b1", "B1复习", "复习")],
}

B1_SETS: list[VocabularySet] = [
    build_set("B1", unit_ref, spec) for unit_ref, specs in _SPECS_BY_UNIT.items() for spec in specs
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
                    definition=f"{level}阶段表达经验和观点时使用的{topic}词汇。",
                    example=f"我可以用{word}表达观点。",
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


B1_SETS += _expanded_sets(
    "B1",
    "b1",
    [
        "意见",
        "原因",
        "结果",
        "经验",
        "变化",
        "关系",
        "帮助",
        "合作",
        "社区",
        "居民",
        "环境",
        "回收",
        "安全",
        "教育",
        "作业",
        "演讲",
        "面试",
        "经历",
        "目标",
        "优点",
        "缺点",
        "问题",
        "解决",
        "科技",
        "网络",
        "信息",
        "文化",
        "历史",
        "社会",
    ],
    ["", "词", "表达", "句子", "问题", "讨论"],
    173,
    36,
)
