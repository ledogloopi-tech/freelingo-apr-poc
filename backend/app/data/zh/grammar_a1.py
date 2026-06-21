"""A1 grammar topics — Mainland Chinese (zh-CN)."""

from app.data._types import GrammarTopic
from app.data.zh.grammar_common import build_topic

_SPECS = [
    ("pinyin-tones", "拼音和声调", "语音", "声母 + 韵母 + 声调", "mā、má、mǎ、mà的声调不同。"),
    ("basic-word-order", "基本语序", "句子结构", "主语 + 谓语 + 宾语", "我喝茶。"),
    ("shi-copula", "是字句", "判断句", "主语 + 是 + 名词", "他是老师。"),
    ("ma-questions", "吗字问句", "疑问句", "陈述句 + 吗", "你是学生吗？"),
    ("pronouns-basic", "基本人称代词", "代词", "我/你/他/她/我们", "我们学习中文。"),
    ("de-possession-basic", "的表示所属", "助词", "名词/代词 + 的 + 名词", "这是我的书。"),
    ("numbers-measure-words", "数字和量词", "数量", "数字 + 量词 + 名词", "我有三个苹果。"),
    ("time-word-order", "时间词位置", "时间", "主语 + 时间 + 动词", "我明天去学校。"),
    ("date-expressions", "日期表达", "时间", "年 + 月 + 日 + 星期", "今天是六月二十一日。"),
    ("zai-location", "在表示位置", "处所", "人/物 + 在 + 地点", "书在桌子上。"),
    ("you-existence", "有表示存在", "存在句", "地点 + 有 + 人/物", "教室里有学生。"),
    ("zhe-na-demonstratives", "这和那", "指示词", "这/那 + 量词 + 名词", "这本书很好。"),
    ("verb-predicate-basic", "动词谓语句", "动词句", "主语 + 动词 + 宾语", "我吃米饭。"),
    ("negative-bu", "不的否定", "否定", "不 + 动词/形容词", "我不喝咖啡。"),
    ("object-placement", "宾语位置", "句子结构", "动词 + 宾语", "她买水果。"),
    ("adjective-predicate", "形容词谓语句", "形容词", "主语 + 很 + 形容词", "今天很热。"),
    ("hen-with-adjectives", "很和形容词", "形容词", "很 + 形容词", "这个房间很安静。"),
    ("like-xihuan", "喜欢表达喜好", "心理动词", "喜欢 + 名词/动词短语", "我喜欢看电影。"),
    ("qing-requests", "请表示请求", "礼貌表达", "请 + 动词", "请坐。"),
    ("measure-word-ge", "个量词", "量词", "数字 + 个 + 名词", "我要两个包子。"),
    ("duoshao-questions", "多少问数量", "疑问词", "多少 + 名词", "这个多少钱？"),
]

A1_GRAMMAR_TOPICS: list[GrammarTopic] = [build_topic("A1", spec) for spec in _SPECS]
