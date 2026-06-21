"""B2 vocabulary sets — Mainland Chinese (zh-CN)."""

from app.data._types import VocabularySet
from app.data.zh.vocabulary_common import build_set

_SPECS_BY_UNIT = {
    "b2-unit-1": [
        ("debate_b2", "讨论辩论", "立场"),
        ("evidence_b2", "证据", "数据"),
        ("society_b2", "社会", "社区"),
    ],
    "b2-unit-2": [
        ("formal_speech_b2", "正式表达", "汇报"),
        ("workplace_b2", "职场", "会议"),
        ("meetings_b2", "会议沟通", "议程"),
    ],
    "b2-unit-3": [
        ("judgement_b2", "判断", "推断"),
        ("news_analysis_b2", "新闻分析", "报道"),
        ("data_trends_b2", "数据趋势", "趋势"),
    ],
    "b2-unit-4": [
        ("cause_effect_b2", "原因和影响", "影响"),
        ("policy_b2", "政策", "措施"),
        ("environment_b2", "环境", "污染"),
    ],
    "b2-unit-5": [
        ("relationships_b2", "复杂关系", "冲突"),
        ("emotions_b2", "情绪", "担心"),
        ("conflict_resolution_b2", "解决冲突", "协商"),
    ],
    "b2-unit-6": [
        ("academic_b2", "学术话题", "概念"),
        ("research_b2", "研究", "调查"),
        ("education_b2", "教育", "课程"),
    ],
    "b2-unit-7": [
        ("media_literacy_b2", "媒体素养", "事实"),
        ("online_discourse_b2", "网络讨论", "评论"),
        ("bias_b2", "偏见", "立场"),
    ],
    "b2-unit-8": [("review_b2", "B2复习", "复习")],
}

B2_SETS: list[VocabularySet] = [
    build_set("B2", unit_ref, spec) for unit_ref, specs in _SPECS_BY_UNIT.items() for spec in specs
]
