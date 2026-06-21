"""B1 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import VocabularySet
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
