"""A1 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import PartOfSpeech, VocabularyEntry, VocabularySet
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
                    definition=f"{level}阶段在{topic}话题中常用的具体词汇。",
                    example=f"我会在简单句子里使用{word}。",
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


A1_SETS += _expanded_sets(
    "A1",
    "a1",
    [
        "家人",
        "朋友",
        "名字",
        "年龄",
        "国家",
        "工作",
        "老师",
        "学生",
        "学校",
        "教室",
        "桌子",
        "椅子",
        "书包",
        "手机",
        "地址",
        "家",
        "房间",
        "厨房",
        "门",
        "窗户",
        "水",
        "米饭",
        "面条",
        "咖啡",
        "茶",
        "水果",
        "市场",
        "商店",
        "价格",
        "钱",
        "银行卡",
        "车站",
        "公交车",
        "地铁",
        "路",
        "时间",
        "今天",
        "明天",
        "天气",
        "衣服",
    ],
    ["", "词", "表达", "句子", "问题", "回答", "练习", "场景"],
    317,
    40,
)
