"""A2 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import VocabularySet
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
