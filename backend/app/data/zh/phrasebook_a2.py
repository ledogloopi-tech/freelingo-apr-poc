"""A2 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "travel_a2",
        "旅行和交通",
        "🚇",
        [
            ("请问地铁站怎么走？", "询问路线", "formal", "a2-unit-7"),
            ("我想买一张去上海的票。", "买车票时", "neutral", "a2-unit-1"),
            ("我需要换乘吗？", "确认交通路线", "neutral", "a2-unit-7"),
        ],
    ),
    (
        "appointments_a2",
        "预约和计划",
        "📅",
        [
            ("我想预约明天下午。", "预约服务", "neutral", "a2-unit-2"),
            ("我们周末见面吧。", "提出计划", "neutral", "a2-unit-2"),
            ("这个时间方便吗？", "确认时间", "formal", "a2-unit-2"),
        ],
    ),
    (
        "health_a2",
        "健康和感受",
        "🩺",
        [
            ("我有点儿不舒服。", "说明身体状况", "neutral", "a2-unit-3"),
            ("我觉得头疼。", "描述症状", "neutral", "a2-unit-3"),
            ("我需要看医生。", "寻求医疗帮助", "neutral", "a2-unit-3"),
        ],
    ),
]

A2_CATEGORIES: list[PhrasebookCategory] = [build_category("A2", spec) for spec in _SPECS]
