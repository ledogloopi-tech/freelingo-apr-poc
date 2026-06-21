"""C2 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "precision_c2",
        "精确表达",
        "🎯",
        [
            ("这个词在这里不只是描述事实，还带有评价意味。", "分析细微语义", "formal", "c2-unit-1"),
            ("为了避免歧义，可以把条件说得更具体。", "提高表达精确度", "formal", "c2-unit-1"),
            ("这个说法语气偏强，可能需要缓和。", "调整表达力度", "formal", "c2-unit-1"),
        ],
    ),
    (
        "mediation_c2",
        "专业中介表达",
        "🔎",
        [
            ("换句话说，这个模型关注的是变化趋势。", "解释专业概念", "formal", "c2-unit-2"),
            ("如果面向非专业读者，需要先说明基本背景。", "调整听众定位", "formal", "c2-unit-2"),
            ("直译能保留结构，但可能失去语用效果。", "说明翻译选择", "formal", "c2-unit-4"),
        ],
    ),
    (
        "editing_c2",
        "高级编辑和改写",
        "✍️",
        [
            ("这段话的信息顺序需要重新安排。", "提出编辑建议", "formal", "c2-unit-7"),
            ("前后段之间缺少清楚的过渡。", "检查篇章衔接", "formal", "c2-unit-7"),
            ("可以删去重复内容，让论证更集中。", "改进文本风格", "formal", "c2-unit-7"),
        ],
    ),
]

C2_CATEGORIES: list[PhrasebookCategory] = [build_category("C2", spec) for spec in _SPECS]
