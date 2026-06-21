"""B2 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "debate_b2",
        "讨论和论证",
        "⚖️",
        [
            ("从数据来看，这个结论还不够充分。", "评价论据", "neutral", "b2-unit-1"),
            ("我理解这个立场，然而风险也需要考虑。", "正式转折", "formal", "b2-unit-7"),
            ("不仅成本会增加，而且执行难度也会上升。", "扩展论证", "neutral", "b2-unit-4"),
        ],
    ),
    (
        "workplace_b2",
        "正式工作沟通",
        "💼",
        [
            ("关于这个问题，我们正在进行评估。", "会议或汇报", "formal", "b2-unit-2"),
            ("请您确认一下会议时间。", "正式确认", "formal", "b2-unit-2"),
            ("根据目前的信息，方案需要调整。", "说明依据", "formal", "b2-unit-6"),
        ],
    ),
    (
        "media_b2",
        "媒体和公共议题",
        "📰",
        [
            ("据报道，相关部门已经回应。", "引用新闻来源", "formal", "b2-unit-7"),
            ("这篇文章的立场比较明显。", "分析媒体文本", "neutral", "b2-unit-7"),
            ("这一变化对公众生活产生了影响。", "说明社会影响", "formal", "b2-unit-4"),
        ],
    ),
]

B2_CATEGORIES: list[PhrasebookCategory] = [build_category("B2", spec) for spec in _SPECS]
