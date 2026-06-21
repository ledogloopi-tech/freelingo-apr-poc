"""C1 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "academic_c1",
        "学术阅读和写作",
        "🎓",
        [
            ("本文主要讨论城市化带来的长期影响。", "概括文章主题", "formal", "c1-unit-3"),
            ("根据研究结果，这一趋势仍将持续。", "引用研究依据", "formal", "c1-unit-3"),
            ("综上所述，问题的核心不只是成本。", "总结观点", "formal", "c1-unit-1"),
        ],
    ),
    (
        "negotiation_c1",
        "协商和说服",
        "🤝",
        [
            ("这个担心有道理，不过我们可以先小范围试行。", "让步后提出方案", "formal", "c1-unit-6"),
            ("如果条件允许，我建议把期限延后一周。", "提出替代方案", "formal", "c1-unit-6"),
            ("我们的目标是在质量和效率之间取得平衡。", "说明协商目标", "formal", "c1-unit-6"),
        ],
    ),
    (
        "culture_c1",
        "文化和文学解读",
        "📖",
        [
            ("这个比喻暗示人物内心的矛盾。", "文学分析", "formal", "c1-unit-7"),
            ("这里的典故需要结合历史背景理解。", "解释文化典故", "formal", "c1-unit-7"),
            ("作者没有明说，但语气中带有批评意味。", "推断隐含信息", "neutral", "c1-unit-7"),
        ],
    ),
]

C1_CATEGORIES: list[PhrasebookCategory] = [build_category("C1", spec) for spec in _SPECS]
