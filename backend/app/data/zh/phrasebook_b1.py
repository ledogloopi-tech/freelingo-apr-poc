"""B1 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "opinions_b1",
        "表达观点",
        "💬",
        [
            ("我认为这个办法比较合适。", "提出个人观点", "neutral", "b1-unit-1"),
            ("我的理由有两个。", "组织论据", "neutral", "b1-unit-1"),
            ("我同意一部分，但还有一个问题。", "部分同意并补充", "neutral", "b1-unit-1"),
        ],
    ),
    (
        "politeness_b1",
        "礼貌请求",
        "🙏",
        [
            ("麻烦你帮我看一下。", "礼貌请求帮助", "formal", "b1-unit-5"),
            ("恐怕我今天不太方便。", "委婉拒绝", "formal", "b1-unit-5"),
            ("能不能再给我一点时间？", "请求延期", "neutral", "b1-unit-5"),
        ],
    ),
    (
        "solutions_b1",
        "问题和解决办法",
        "🛠️",
        [
            ("问题可能出在网络上。", "分析问题原因", "neutral", "b1-unit-7"),
            ("我们可以先试试这个方法。", "提出解决办法", "neutral", "b1-unit-7"),
            ("如果还不行，我再联系维修。", "说明备选方案", "neutral", "b1-unit-7"),
        ],
    ),
]

B1_CATEGORIES: list[PhrasebookCategory] = [build_category("B1", spec) for spec in _SPECS]
