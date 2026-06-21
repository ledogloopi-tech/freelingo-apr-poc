"""C2 grammar topics — Mainland Chinese (zh-CN)."""

from app.data._types import GrammarTopic
from app.data.zh.grammar_common import build_topic

_SPECS = [
    (
        "semantic-precision-zh",
        "语义精确",
        "高级语义",
        "近义表达 + 语境差异",
        "“可能”和“或许”的语气强度不完全相同。",
    ),
    (
        "xuci-nuance",
        "虚词细微差别",
        "语气",
        "虚词 + 语气/立场",
        "“倒是”常带有转折或重新评价的意味。",
    ),
    (
        "word-choice-register-zh",
        "词语选择和语体",
        "语体",
        "词义 + 场合 + 关系",
        "“协助”比“帮忙”更正式。",
    ),
    (
        "expert-mediation-zh",
        "专业内容中介",
        "中介表达",
        "专业概念 + 通俗解释",
        "换句话说，这个模型是在预测趋势。",
    ),
    (
        "reformulation-zh",
        "重新表述",
        "改写",
        "原意 + 新结构 + 保持重点",
        "也就是说，问题不在速度，而在稳定性。",
    ),
    (
        "audience-adaptation-zh",
        "面向听众调整",
        "表达策略",
        "听众背景 + 解释深度",
        "如果面对初学者，需要先解释基本概念。",
    ),
    (
        "critical-evaluation-zh",
        "批判评价",
        "批判思维",
        "评价标准 + 证据 + 判断",
        "这个结论有价值，但样本范围有限。",
    ),
    ("qian-ti-analysis", "前提分析", "论证", "找出隐含前提", "这个观点假设所有人都有同样的资源。"),
    ("fanbo-structure", "反驳结构", "论证", "对方观点 + 反证 + 新结论", "这种说法忽略了长期成本。"),
    (
        "translation-equivalence-zh",
        "翻译等值",
        "翻译",
        "意义 + 功能 + 语气",
        "有些表达不能只按字面翻译。",
    ),
    (
        "pragmatic-meaning-zh",
        "语用意义",
        "语用",
        "字面意义 + 交际意图",
        "“有空再说”有时表示委婉拒绝。",
    ),
    (
        "cultural-transfer-zh",
        "跨文化转换",
        "文化",
        "文化概念 + 解释 + 适配",
        "需要先说明背景，读者才能理解典故。",
    ),
    (
        "rhetorical-strategy-zh",
        "修辞策略",
        "修辞",
        "目的 + 读者 + 手段",
        "先提出问题，再用对比增强说服力。",
    ),
    (
        "emphasis-control-zh",
        "强调控制",
        "表达力度",
        "强调词 + 句式 + 语境",
        "过度强调可能让语气显得生硬。",
    ),
    (
        "reader-positioning-zh",
        "读者定位",
        "写作策略",
        "预设读者 + 引导理解",
        "作者把读者放在共同思考的位置。",
    ),
    (
        "language-history-zh",
        "语言历史",
        "语言变化",
        "历史语境 + 当前用法",
        "有些词保留了古汉语色彩。",
    ),
    (
        "chengyu-register",
        "成语语体",
        "成语",
        "成语 + 场合 + 风格",
        "正式演讲中使用成语可以增强凝练感。",
    ),
    (
        "diachronic-change-zh",
        "历时变化",
        "语言变化",
        "过去用法 + 现代用法",
        "词义会随着社会变化而扩展。",
    ),
    ("advanced-editing-zh", "高级编辑", "编辑", "内容 + 结构 + 语言", "这段话需要删去重复信息。"),
    (
        "cohesion-coherence-zh",
        "衔接和连贯",
        "篇章",
        "连接词 + 指代 + 信息顺序",
        "前后段需要更清楚的过渡。",
    ),
    (
        "style-revision-zh",
        "文体修改",
        "改写",
        "目的 + 读者 + 语体一致",
        "把口语化表达改成正式书面语。",
    ),
]

C2_GRAMMAR_TOPICS: list[GrammarTopic] = [build_topic("C2", spec) for spec in _SPECS]
