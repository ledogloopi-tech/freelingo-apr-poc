"""A2 grammar topics — Mainland Chinese (zh-CN)."""

from app.data._types import GrammarTopic
from app.data.zh.grammar_common import build_topic

_SPECS = [
    ("le-completed-action", "了表示完成", "体貌", "动词 + 了 + 宾语", "我昨天看了电影。"),
    ("guo-experience", "过表示经历", "体貌", "动词 + 过", "我去过北京。"),
    ("time-sequence", "时间顺序", "篇章连接", "先……再/然后……", "我先吃饭，然后去上课。"),
    ("yao-future", "要表示将来", "将来", "要 + 动词", "我明天要去医院。"),
    ("hui-ability-future", "会表示能力和可能", "情态", "会 + 动词", "他会说中文。"),
    ("dasuan-plans", "打算表达计划", "计划", "打算 + 动词", "我打算周末休息。"),
    ("yinwei-suoyi", "因为所以", "因果", "因为……所以……", "因为下雨，所以我不出门。"),
    ("danshi-turn", "但是转折", "转折", "句子 + 但是 + 句子", "这家店贵，但是很好吃。"),
    ("feelings-with-jue-de", "觉得表达感受", "心理动词", "觉得 + 句子/形容词", "我觉得今天很冷。"),
    ("keyi-permission", "可以表示允许", "情态", "可以 + 动词", "这里可以拍照吗？"),
    ("bu-neng-prohibition", "不能表示禁止", "情态", "不能 + 动词", "这里不能吸烟。"),
    ("dei-must", "得表示必须", "情态", "得 + 动词", "我得早点走。"),
    ("bi-comparison", "比字比较", "比较", "A + 比 + B + 形容词", "上海比这里大。"),
    ("gen-yi-yang", "跟一样", "比较", "A + 跟 + B + 一样 + 形容词", "这个颜色跟那个一样好看。"),
    ("zui-superlative", "最表示最高程度", "程度", "最 + 形容词", "这家店最好。"),
    ("zai-progressive", "正在进行", "进行", "正在 + 动词", "我正在写作业。"),
    ("zhe-duration-state", "着表示持续", "状态", "动词 + 着", "门开着。"),
    ("le-change-of-state", "句末了表示变化", "变化", "句子 + 了", "天气冷了。"),
    ("dao-direction", "到表示到达", "方向", "动词 + 到 + 地点", "我走到车站。"),
    ("verb-yixia", "一下表示短暂", "语气", "动词 + 一下", "请等一下。"),
    ("try-kan-kan", "看看表示尝试", "尝试", "动词 + 看看", "你试试看。"),
]

A2_GRAMMAR_TOPICS: list[GrammarTopic] = [build_topic("A2", spec) for spec in _SPECS]
