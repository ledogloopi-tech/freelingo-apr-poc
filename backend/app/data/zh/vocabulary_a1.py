"""A1 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import VocabularySet
from app.data.zh.vocabulary_common import build_set

_SPECS_BY_UNIT = {
    "a1-unit-1": [
        ("pinyin_a1", "拼音", "拼音"),
        ("greetings_a1", "问候", "你好"),
        ("classroom_a1", "课堂", "教室"),
    ],
    "a1-unit-2": [
        ("identity_a1", "身份信息", "姓名"),
        ("countries_a1", "国家", "中国"),
        ("occupations_a1", "职业", "老师"),
    ],
    "a1-unit-3": [
        ("numbers_a1", "数字", "数字"),
        ("time_a1", "时间", "时间"),
        ("days_dates_a1", "日期", "今天"),
    ],
    "a1-unit-4": [
        ("places_a1", "地点", "学校"),
        ("home_a1", "家", "房间"),
        ("city_a1", "城市", "街道"),
    ],
    "a1-unit-5": [
        ("daily_routine_a1", "日常生活", "早上"),
        ("food_a1", "食物", "米饭"),
        ("transport_a1", "交通", "地铁"),
    ],
    "a1-unit-6": [
        ("adjectives_a1", "形容词", "好"),
        ("hobbies_a1", "爱好", "电影"),
        ("weather_a1", "天气", "下雨"),
    ],
    "a1-unit-7": [
        ("shopping_a1", "购物", "价格"),
        ("requests_a1", "请求", "请"),
        ("directions_a1", "方向", "左边"),
    ],
    "a1-unit-8": [("review_a1", "A1复习", "复习")],
}

A1_SETS: list[VocabularySet] = [
    build_set("A1", unit_ref, spec) for unit_ref, specs in _SPECS_BY_UNIT.items() for spec in specs
]
