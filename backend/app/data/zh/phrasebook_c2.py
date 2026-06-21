"""C2 phrasebook categories — Mainland Chinese (zh-CN)."""

from app.data._types import PhrasebookCategory
from app.data.zh.phrasebook_common import build_category

_SPECS = [
    (
        "precision_c2",
        "精确表达和调整",
        "🎯",
        [
            ("这个词在这里不只是描述事实，还带有评价意味。", "分析细微语义", "formal", "c2-unit-1", "Zhège cí zài zhèlǐ bùzhǐ shì miáoshù shìshí, hái dài yǒu píngjià yìwèi."),
            ("为了避免歧义，可以把条件说得更具体。", "提高表达精确度", "formal", "c2-unit-1", "Wèile bìmiǎn qíyì, kěyǐ bǎ tiáojiàn shuō de gèng jùtǐ."),
            ("这个说法语气偏强，可能需要缓和。", "调整表达力度", "formal", "c2-unit-1", "Zhège shuōfǎ yǔqì piān qiáng, kěnéng xūyào huǎnhé."),
            ("严格来说，需要区分两个条件。", "严格区分条件", "formal", "c2-unit-1", "Yángé lái shuō, xūyào qūfēn liǎng ge tiáojiàn."),
            ("不能混淆相关关系和因果关系。", "区分相关与因果", "formal", "c2-unit-1", "Bù néng hùnxiáo xiāngguān guānxi hé yīnguǒ guānxi."),
            ("这个概念需要更清晰的边界。", "要求明确概念边界", "formal", "c2-unit-1", "Zhège gàiniàn xūyào gèng qīngxī de biānjiè."),
        ],
    ),
    (
        "mediation_c2",
        "专业中介表达",
        "🔍",
        [
            ("换句话说，这个模型关注的是变化趋势。", "解释专业概念", "formal", "c2-unit-2", "Huàn jù huà shuō, zhège móxíng guānzhù de shì biànhuà qūshì."),
            ("如果面向非专业读者，需要先说明基本背景。", "调整听众定位", "formal", "c2-unit-2", "Rúguǒ miànxiàng fēi zhuānyè dúzhě, xūyào xiān shuōmíng jīběn bèijǐng."),
            ("直译能保留结构，但可能失去语用效果。", "说明翻译选择", "formal", "c2-unit-4", "Zhíyì néng bǎoliú jiégòu, dàn kěnéng shīqù yǔyòng xiàoguǒ."),
            ("我会避开专业术语重新解释。", "简化专业表达", "formal", "c2-unit-2", "Wǒ huì bìkāi zhuānyè shùyǔ chóngxīn jiěshì."),
            ("补充背景知识后更容易理解。", "建议补充背景", "formal", "c2-unit-2", "Bǔchōng bèijǐng zhīshi hòu gèng róngyì lǐjiě."),
            ("说明方式需要根据听众调整。", "强调听众适应", "formal", "c2-unit-2", "Shuōmíng fāngshì xūyào gēnjù tīngzhòng tiáozhěng."),
        ],
    ),
    (
        "editing_c2",
        "高级编辑和改写",
        "✍️",
        [
            ("这段话的信息顺序需要重新安排。", "提出编辑建议", "formal", "c2-unit-7", "Zhè duàn huà de xìnxī shùnxù xūyào chóngxīn ānpái."),
            ("前后段之间缺少清楚的过渡。", "检查篇章衔接", "formal", "c2-unit-7", "Qián hòu duàn zhījiān quēshǎo qīngchu de guòdù."),
            ("可以删去重复内容，让论证更集中。", "改进文本风格", "formal", "c2-unit-7", "Kěyǐ shān qù chóngfù nèiróng, ràng lùnzhèng gèng jízhōng."),
            ("重新排列论点会更有说服力。", "重组论证结构", "formal", "c2-unit-7", "Chóngxīn páiliè lùndiǎn huì gèng yǒu shuōfúlì."),
            ("降低表达强度会显得更平衡。", "调整语气强度", "formal", "c2-unit-7", "Jiàngdī biǎodá qiángdù huì xiǎnde gèng pínghéng."),
            ("我会把讨论重构得更精确。", "承诺精确重构", "formal", "c2-unit-7", "Wǒ huì bǎ tǎolùn chónggòu de gèng jīngquè."),
        ],
    ),
    (
        "synthesis_c2",
        "综合和批判性思维",
        "🧩",
        [
            ("整合多个立场后，可以得出不同结论。", "综合多方立场", "formal", "c2-unit-8", "Zhěnghé duō ge lìchǎng hòu, kěyǐ déchū bùtóng jiélùn."),
            ("这个主张的前提还没有充分验证。", "质疑前提", "formal", "c2-unit-8", "Zhège zhǔzhāng de qiántí hái méiyǒu chōngfèn yànzhèng."),
            ("加入反证案例后，结论会更加有限。", "引入反证审视", "formal", "c2-unit-8", "Jiārù fǎnzhèng ànlì hòu, jiélùn huì gèngjiā yǒuxiàn."),
            ("仅凭这些资料还不能断定。", "指出证据不足", "formal", "c2-unit-8", "Jǐn píng zhèxiē zīliào hái bù néng duàndìng."),
            ("纳入反对意见可以增强论证。", "建议纳入反方", "formal", "c2-unit-8", "Nàrù fǎnduì yìjiàn kěyǐ zēngqiáng lùnzhèng."),
            ("这只是多种解释中的一种。", "保持解释开放性", "neutral", "c2-unit-8", "Zhè zhǐshì duō zhǒng jiěshì zhōng de yì zhǒng."),
        ],
    ),
    (
        "translation_c2",
        "翻译与语际转化",
        "🌐",
        [
            ("直译不自然，所以采用了功能上接近的表达。", "解释翻译策略", "formal", "c2-unit-4", "Zhíyì bú zìrán, suǒyǐ cǎiyòng le gōngnéng shang jiējìn de biǎodá."),
            ("文体和礼貌程度也需要一起转化。", "讨论文体转换", "formal", "c2-unit-4", "Wéntǐ hé lǐmào chéngdù yě xūyào yìqǐ zhuǎnhuà."),
            ("补充文化背景后，意思会更清楚。", "文化背景补充", "formal", "c2-unit-4", "Bǔchōng wénhuà bèijǐng hòu, yìsi huì gèng qīngchu."),
            ("原文和译文的效果并不完全相同。", "讨论翻译效果", "formal", "c2-unit-4", "Yuánwén hé yìwén de xiàoguǒ bìng bù wánquán xiāngtóng."),
            ("我在不损害原文含义的范围内进行了重构。", "说明重构原则", "formal", "c2-unit-4", "Wǒ zài bù sǔnhài yuánwén hányì de fànwéi nèi jìnxíng le chónggòu."),
            ("我们需要同时考虑语言效果和事实准确性。", "强调双重标准", "formal", "c2-unit-4", "Wǒmen xūyào tóngshí kǎolǜ yǔyán xiàoguǒ hé shìshí zhǔnquèxìng."),
        ],
    ),
]

C2_CATEGORIES: list[PhrasebookCategory] = [build_category("C2", spec) for spec in _SPECS]
