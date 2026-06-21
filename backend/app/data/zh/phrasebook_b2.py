"""B2 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "debate_b2",
        "讨论和论证",
        "⚖️",
        [
            ("从数据来看，这个结论还不够充分。", "评价论据", "neutral", "b2-unit-1", "Cóng shùjù lái kàn, zhège jiélùn hái búgòu chōngfèn."),
            ("我理解这个立场，然而风险也需要考虑。", "正式转折", "formal", "b2-unit-7", "Wǒ lǐjiě zhège lìchǎng, rán'ér fēngxiǎn yě xūyào kǎolǜ."),
            ("不仅成本会增加，而且执行难度也会上升。", "扩展论证", "neutral", "b2-unit-4", "Bùjǐn chéngběn huì zēngjiā, érqiě zhíxíng nándù yě huì shàngshēng."),
            ("这个观点有一定说服力。", "评价观点力度", "neutral", "b2-unit-1", "Zhège guāndiǎn yǒu yídìng shuōfúlì."),
            ("不过，它的前提还有点弱。", "指出前提不足", "neutral", "b2-unit-1", "Búguò, tā de qiántí hái yǒudiǎn ruò."),
            ("如果加上具体例子会更好。", "建议补充例证", "neutral", "b2-unit-1", "Rúguǒ jiāshang jùtǐ lìzi huì gèng hǎo."),
        ],
    ),
    (
        "workplace_b2",
        "正式工作沟通",
        "💼",
        [
            ("关于这个问题，我们正在进行评估。", "会议或汇报", "formal", "b2-unit-2", "Guānyú zhège wèntí, wǒmen zhèngzài jìnxíng pínggū."),
            ("请您确认一下会议时间。", "正式确认", "formal", "b2-unit-2", "Qǐng nín quèrèn yíxià huìyì shíjiān."),
            ("根据目前的信息，方案需要调整。", "说明依据", "formal", "b2-unit-6", "Gēnjù mùqián de xìnxī, fāng'àn xūyào tiáozhěng."),
            ("我会和相关部门协调。", "承诺协调", "formal", "b2-unit-2", "Wǒ huì hé xiāngguān bùmén xiétiáo."),
            ("我会把共识写进会议记录。", "记录共识", "formal", "b2-unit-2", "Wǒ huì bǎ gòngshí xiě jìn huìyì jìlù."),
            ("决定之前还需要进一步讨论。", "建议推迟决定", "formal", "b2-unit-2", "Juédìng zhīqián hái xūyào jìnyíbù tǎolùn."),
        ],
    ),
    (
        "media_b2",
        "媒体和公共议题",
        "📰",
        [
            ("据报道，相关部门已经回应。", "引用新闻来源", "formal", "b2-unit-7", "Jù bàodào, xiāngguān bùmén yǐjīng huíyìng."),
            ("这篇文章的立场比较明显。", "分析媒体文本", "neutral", "b2-unit-7", "Zhè piān wénzhāng de lìchǎng bǐjiào míngxiǎn."),
            ("这一变化对公众生活产生了影响。", "说明社会影响", "formal", "b2-unit-4", "Zhè yí biànhuà duì gōngzhòng shēnghuó chǎnshēng le yǐngxiǎng."),
            ("还需要确认专家的意见。", "提出需要专家确认", "neutral", "b2-unit-7", "Hái xūyào quèrèn zhuānjiā de yìjiàn."),
            ("要区分事实和观点。", "提醒区分事实观点", "neutral", "b2-unit-7", "Yào qūfēn shìshí hé guāndiǎn."),
            ("对不同群体的影响不一样。", "说明不同影响", "neutral", "b2-unit-4", "Duì bùtóng qúntǐ de yǐngxiǎng bù yíyàng."),
        ],
    ),
    (
        "analysis_b2",
        "分析和写作",
        "📈",
        [
            ("我们需要根据目前的情况来判断。", "提出判断基础", "formal", "b2-unit-8", "Wǒmen xūyào gēnjù mùqián de qíngkuàng lái pànduàn."),
            ("解读统计数据时要注意方法。", "提醒分析方法", "neutral", "b2-unit-8", "Jiědú tǒngjì shùjù shí yào zhùyì fāngfǎ."),
            ("核心信息最好放在前面。", "写作建议", "neutral", "b2-unit-8", "Héxīn xìnxī zuìhǎo fàng zài qiánmiàn."),
            ("结论需要写得更清楚。", "编辑建议", "neutral", "b2-unit-8", "Jiélùn xūyào xiě de gèng qīngchu."),
            ("也要考虑读者的反应。", "提醒读者意识", "neutral", "b2-unit-8", "Yě yào kǎolǜ dúzhě de fǎnyìng."),
            ("这个表达需要更正式一些。", "修改建议", "neutral", "b2-unit-8", "Zhège biǎodá xūyào gèng zhèngshì yìxiē."),
        ],
    ),
    (
        "negotiation_risk_b2",
        "协商与风险管理",
        "🔍",
        [
            ("需要确认成本和效果的关系。", "提出分析要点", "formal", "b2-unit-8", "Xūyào quèrèn chéngběn hé xiàoguǒ de guānxì."),
            ("风险因素应该提前分享。", "建议提前沟通", "formal", "b2-unit-8", "Fēngxiǎn yīnsù yīnggāi tíqián fēnxiǎng."),
            ("我建议先做小范围测试。", "建议试点", "formal", "b2-unit-8", "Wǒ jiànyì xiān zuò xiǎo fànwéi cèshì."),
            ("这个政策需要逐步实施。", "建议分步实施", "formal", "b2-unit-8", "Zhège zhèngcè xūyào zhúbù shíshī."),
            ("但是长期效果还不确定。", "指出不确定性", "neutral", "b2-unit-8", "Dànshì chángqī xiàoguǒ hái bú quèdìng."),
            ("我们可以保留这个替代方案。", "保留备选", "neutral", "b2-unit-8", "Wǒmen kěyǐ bǎoliú zhège tìdài fāng'àn."),
        ],
    ),
]

B2_CATEGORIES: list[PhrasebookCategory] = [build_category("B2", spec) for spec in _SPECS]
