"""A1 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "greetings_a1",
        "问候和介绍",
        "👋",
        [
            ("你好。", "见面时打招呼", "neutral", "a1-unit-1"),
            ("我叫李明。", "介绍自己的名字", "neutral", "a1-unit-2"),
            ("很高兴认识你。", "初次见面时表达友好", "neutral", "a1-unit-2"),
        ],
    ),
    (
        "classroom_a1",
        "课堂表达",
        "📚",
        [
            ("请再说一遍。", "没听清时", "formal", "a1-unit-1"),
            ("我有一个问题。", "课堂上提问", "neutral", "a1-unit-1"),
            ("我不太明白。", "表达没有理解", "neutral", "a1-unit-1"),
        ],
    ),
    (
        "shopping_a1",
        "基础购物",
        "🛒",
        [
            ("这个多少钱？", "询问价格", "neutral", "a1-unit-7"),
            ("我要这个。", "选择商品", "neutral", "a1-unit-7"),
            ("可以刷卡吗？", "询问付款方式", "neutral", "a1-unit-7"),
        ],
    ),
]

A1_CATEGORIES: list[PhrasebookCategory] = [build_category("A1", spec) for spec in _SPECS]
