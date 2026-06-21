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

A1_CATEGORIES.append(
    build_category(
        "A1",
        (
            "expanded_daily_a1",
            "基础生活表达",
            "🏠",
            [
                (text, "基础生活场景中的常用表达", "neutral", "a1-unit-8")
                for text in [
                    "洗手间在哪里？",
                    "我需要水。",
                    "请说慢一点。",
                    "请再说一次。",
                    "这个中文怎么说？",
                    "我听不清楚。",
                    "我可以坐这里吗？",
                    "可以开窗吗？",
                    "今天天气很好。",
                    "有点冷。",
                    "有点热。",
                    "这条路对吗？",
                    "到车站近吗？",
                    "公交站在哪里？",
                    "这辆车去市中心吗？",
                    "请给我一张票。",
                    "我在这里下车吗？",
                    "可以拍照吗？",
                    "请写一下名字。",
                    "请告诉我电话号码。",
                    "这是我的电话号码。",
                    "我丢了包。",
                    "请帮帮我。",
                    "没关系。",
                    "对不起。",
                    "谢谢。",
                    "非常感谢。",
                    "等一下。",
                    "我现在很忙。",
                    "我们以后见。",
                    "你明天有时间吗？",
                    "我们一起去吧。",
                    "我饿了。",
                    "我渴了。",
                    "请给我菜单。",
                    "这个很好吃。",
                    "请不要太辣。",
                    "请结账。",
                    "请给我一个袋子。",
                    "我用现金付。",
                    "我用卡付。",
                    "请给我收据。",
                    "我喜欢这个颜色。",
                    "请给我看看别的。",
                    "我今天第一次来。",
                    "我还会再来。",
                    "请在这里等我。",
                    "祝你今天愉快。",
                    "我住在附近。",
                    "这是谁的手机？",
                    "请小心。",
                    "明天见。",
                ]
            ],
        ),
    )
)
