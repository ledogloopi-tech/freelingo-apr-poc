"""C1 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "academic_c1",
        "学术阅读和写作",
        "🎓",
        [
            ("本文主要讨论城市化带来的长期影响。", "概括文章主题", "formal", "c1-unit-3", "Běnwén zhǔyào tǎolùn chéngshìhuà dàilái de chángqī yǐngxiǎng."),
            ("根据研究结果，这一趋势仍将持续。", "引用研究依据", "formal", "c1-unit-3", "Gēnjù yánjiū jiéguǒ, zhè yì qūshì réng jiāng chíxù."),
            ("综上所述，问题的核心不只是成本。", "总结观点", "formal", "c1-unit-1", "Zōng shàng suǒ shù, wèntí de héxīn bùzhǐ shì chéngběn."),
            ("调查方法有几个限制。", "说明研究局限", "formal", "c1-unit-3", "Diàochá fāngfǎ yǒu jǐ ge xiànzhì."),
            ("解释结果时需要谨慎。", "提醒谨慎解读", "formal", "c1-unit-3", "Jiěshì jiéguǒ shí xūyào jǐnshèn."),
            ("也要保留其他解释的可能性。", "保持学术开放性", "formal", "c1-unit-3", "Yě yào bǎoliú qítā jiěshì de kěnéngxìng."),
        ],
    ),
    (
        "negotiation_c1",
        "协商和说服",
        "🤝",
        [
            ("这个担心有道理，不过我们可以先小范围试行。", "让步后提出方案", "formal", "c1-unit-6", "Zhège dānxīn yǒu dàolǐ, búguò wǒmen kěyǐ xiān xiǎo fànwéi shìxíng."),
            ("如果条件允许，我建议把期限延后一周。", "提出替代方案", "formal", "c1-unit-6", "Rúguǒ tiáojiàn yǔnxǔ, wǒ jiànyì bǎ qīxiàn yánhòu yì zhōu."),
            ("我们的目标是在质量和效率之间取得平衡。", "说明协商目标", "formal", "c1-unit-6", "Wǒmen de mùbiāo shì zài zhìliàng hé xiàolǜ zhījiān qǔdé pínghéng."),
            ("我们充分理解对方的担忧。", "表示理解", "formal", "c1-unit-6", "Wǒmen chōngfèn lǐjiě duìfāng de dānyōu."),
            ("但也必须考虑现实限制。", "提出现实限制", "formal", "c1-unit-6", "Dàn yě bìxū kǎolǜ xiànshí xiànzhì."),
            ("我希望找到双方都能接受的方案。", "表达协商意向", "formal", "c1-unit-6", "Wǒ xīwàng zhǎodào shuāngfāng dōu néng jiēshòu de fāng'àn."),
        ],
    ),
    (
        "culture_c1",
        "文化和文学解读",
        "📖",
        [
            ("这个比喻暗示人物内心的矛盾。", "文学分析", "formal", "c1-unit-7", "Zhège bǐyù ànshì rénwù nèixīn de máodùn."),
            ("这里的典故需要结合历史背景理解。", "解释文化典故", "formal", "c1-unit-7", "Zhèlǐ de diǎngù xūyào jiéhé lìshǐ bèijǐng lǐjiě."),
            ("作者没有明说，但语气中带有批评意味。", "推断隐含信息", "neutral", "c1-unit-7", "Zuòzhě méiyǒu míng shuō, dàn yǔqì zhōng dài yǒu pīpíng yìwèi."),
            ("这种表达在不同语境中可能有不同解释。", "讨论语境影响", "formal", "c1-unit-7", "Zhè zhǒng biǎodá zài bùtóng yǔjìng zhōng kěnéng yǒu bùtóng jiěshì."),
            ("用更委婉的方式表达会更合适。", "建议委婉表达", "formal", "c1-unit-7", "Yòng gèng wěiwǎn de fāngshì biǎodá huì gèng héshì."),
            ("这个说法可能显得过于直接。", "评价表达方式", "neutral", "c1-unit-7", "Zhège shuōfǎ kěnéng xiǎnde guòyú zhíjiē."),
        ],
    ),
    (
        "precision_c1",
        "精细表达和前提",
        "🎚️",
        [
            ("在下结论之前，我想确认前提。", "确认前提", "formal", "c1-unit-8", "Zài xià jiélùn zhīqián, wǒ xiǎng quèrèn qiántí."),
            ("我们先定义术语，再开始讨论。", "提议定义术语", "formal", "c1-unit-8", "Wǒmen xiān dìngyì shùyǔ, zài kāishǐ tǎolùn."),
            ("关键是区分原因和结果。", "强调因果关系", "formal", "c1-unit-8", "Guānjiàn shì qūfēn yuányīn hé jiéguǒ."),
            ("我们先区分事实和评价。", "区分事实和评价", "formal", "c1-unit-8", "Wǒmen xiān qūfēn shìshí hé píngjià."),
            ("结论最好以有条件的方式提出。", "建议条件式结论", "formal", "c1-unit-8", "Jiélùn zuìhǎo yǐ yǒu tiáojiàn de fāngshì tíchū."),
            ("我们需要避免过度概括。", "提醒避免过度概括", "formal", "c1-unit-8", "Wǒmen xūyào bìmiǎn guòdù gàikuò."),
        ],
    ),
    (
        "decision_c1",
        "决策与责任",
        "⚖️",
        [
            ("这个选择合理，但需要管理风险。", "评价选择的合理性", "formal", "c1-unit-8", "Zhège xuǎnzé hélǐ, dàn xūyào guǎnlǐ fēngxiǎn."),
            ("不能只根据短期利益来判断。", "反对短视判断", "formal", "c1-unit-8", "Bù néng zhǐ gēnjù duǎnqī lìyì lái pànduàn."),
            ("这个决定关系到长期责任。", "强调长期责任", "formal", "c1-unit-8", "Zhège juédìng guānxi dào chángqī zérèn."),
            ("责任范围需要以书面形式确认。", "要求书面确认", "formal", "c1-unit-8", "Zérèn fànwéi xūyào yǐ shūmiàn xíngshì quèrèn."),
            ("我会考虑对方的意图再回答。", "谨慎回应", "formal", "c1-unit-8", "Wǒ huì kǎolǜ duìfāng de yìtú zài huídá."),
            ("等判断材料充分以后再决定。", "建议延期决定", "formal", "c1-unit-8", "Děng pànduàn cáiliào chōngfèn yǐhòu zài juédìng."),
        ],
    ),
]

C1_CATEGORIES: list[PhrasebookCategory] = [build_category("C1", spec) for spec in _SPECS]
