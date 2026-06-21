"""A2 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import PartOfSpeech, VocabularyEntry, VocabularySet
from app.data.zh.vocabulary_common import build_set

_SPECS_BY_UNIT = {
    "a2-unit-1": [
        ("past_events_a2", "过去经历", "昨天"),
        ("travel_a2", "旅行", "火车"),
        ("weekend_a2", "周末", "周末"),
    ],
    "a2-unit-2": [
        ("plans_a2", "计划", "打算"),
        ("appointments_a2", "预约", "预约"),
        ("calendar_a2", "日程", "日历"),
    ],
    "a2-unit-3": [
        ("reasons_a2", "原因", "因为"),
        ("feelings_a2", "感受", "高兴"),
        ("health_a2", "健康", "医生"),
    ],
    "a2-unit-4": [
        ("rules_a2", "规则", "规定"),
        ("public_places_a2", "公共场所", "图书馆"),
        ("work_school_a2", "工作和学习", "办公室"),
    ],
    "a2-unit-5": [
        ("comparisons_a2", "比较", "更好"),
        ("shopping_choices_a2", "购物选择", "选择"),
        ("food_review_a2", "食物评价", "味道"),
    ],
    "a2-unit-6": [
        ("activities_a2", "活动", "运动"),
        ("home_tasks_a2", "家务", "打扫"),
        ("technology_a2", "科技", "手机"),
    ],
    "a2-unit-7": [
        ("directions_a2", "路线", "路口"),
        ("services_a2", "服务", "服务台"),
        ("transport_detail_a2", "交通细节", "换乘"),
    ],
    "a2-unit-8": [("review_a2", "A2复习", "复习")],
}

A2_SETS: list[VocabularySet] = [
    build_set("A2", unit_ref, spec) for unit_ref, specs in _SPECS_BY_UNIT.items() for spec in specs
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
                    definition=f"{level}阶段在{topic}话题中描述具体情况的词汇。",
                    example=f"请在真实场景中使用{word}说明情况。",
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


A2_SETS += _expanded_sets(
    "A2",
    "a2",
    [
        "预订",
        "旅行",
        "酒店",
        "机场",
        "行李",
        "车票",
        "换乘",
        "约会",
        "计划",
        "经历",
        "健康",
        "医院",
        "药",
        "运动",
        "家务",
        "修理",
        "购物",
        "收据",
        "退货",
        "邀请",
        "聚会",
        "照片",
        "服务",
        "表格",
    ],
    ["", "词", "表达", "句子", "问题", "情况"],
    142,
    36,
)
