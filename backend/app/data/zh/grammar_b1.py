"""B1 grammar topics — Mainland Chinese (zh-CN)."""

from app.data._types import GrammarTopic
from app.data.zh.grammar_common import build_topic

_SPECS = [
    ("wo-renwei-opinion", "我认为表达观点", "观点", "我认为 + 句子", "我认为这个办法很好。"),
    ("dui-topic", "对引出对象", "话题", "对 + 对象 + 来说", "对我来说，学习很重要。"),
    ("reason-erqie", "而且补充理由", "连接", "句子 + 而且 + 句子", "这里方便，而且不贵。"),
    (
        "yi-bian-yi-bian",
        "一边一边",
        "同时动作",
        "一边 + 动词，一边 + 动词",
        "他一边听音乐，一边做饭。",
    ),
    ("xian-ranhou", "先然后", "顺序", "先 + 动作，然后 + 动作", "我先洗衣服，然后做饭。"),
    ("de-shihou", "的时候", "时间背景", "动词/句子 + 的时候", "我上大学的时候学过中文。"),
    ("yinggai-advice", "应该表示建议", "建议", "应该 + 动词", "你应该早点休息。"),
    ("zuihao-suggestion", "最好表示建议", "建议", "最好 + 动词", "你最好提前预约。"),
    ("huozhe-choice", "或者表示选择", "选择", "A + 或者 + B", "我们坐地铁或者打车。"),
    ("ruguo-jiu", "如果就", "条件", "如果……就……", "如果明天下雨，我们就不去。"),
    ("yaoshi-condition", "要是条件", "条件", "要是……就……", "要是你有时间，就给我打电话。"),
    ("keneng-maybe", "可能表示不确定", "推测", "可能 + 动词/形容词", "他可能迟到。"),
    ("neng-buneng-request", "能不能请求", "请求", "能不能 + 动词", "你能不能帮我一下？"),
    ("mafan-ni", "麻烦你", "礼貌表达", "麻烦你 + 动词", "麻烦你帮我打印一下。"),
    ("kongpa-refusal", "恐怕委婉拒绝", "委婉", "恐怕 + 句子", "恐怕我今天不能参加。"),
    ("suiran-danshi", "虽然但是", "让步", "虽然……但是……", "虽然很累，但是我很高兴。"),
    ("yue-lai-yue", "越来越", "变化", "越来越 + 形容词", "天气越来越热。"),
    ("ba-sentence-intro", "把字句入门", "处置", "把 + 宾语 + 动词", "请把门关上。"),
    ("bei-passive-intro", "被字句入门", "被动", "被 + 施事 + 动词", "我的手机被他拿走了。"),
    ("ba-result", "把字句结果", "处置", "把 + 宾语 + 动词 + 结果", "我把作业写完了。"),
    ("weile-purpose", "为了表示目的", "目的", "为了 + 目的", "为了健康，我每天运动。"),
]

B1_GRAMMAR_TOPICS: list[GrammarTopic] = [build_topic("B1", spec) for spec in _SPECS]
