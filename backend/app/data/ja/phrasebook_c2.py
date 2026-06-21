"""C2 phrasebook categories — Japanese (ja-JP)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry


def _p(text: str, context: str, register: str, unit_ref: str | None = None) -> PhrasebookEntry:
    return PhrasebookEntry(
        text=text,
        context=context,
        register=register,  # type: ignore[arg-type]
        unit_ref=unit_ref,
    )


C2_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id='mediation_ja_c2',
        level='C2',
        situation='仲介と専門説明',
        icon='🌐',
        phrases=[
            _p('専門用語を避けて言い換えると、次のようになります。', '分かりやすく言い換える', 'formal', 'c2-unit-3'),
            _p('原文のニュアンスを保つなら、この表現が近いです。', '翻訳の選択を説明する', 'formal', 'c2-unit-3'),
            _p('この議論の前提には、二つの価値判断があります。', '前提を分析する', 'formal', 'c2-unit-7'),
            _p('複数の資料を照合すると、異なる結論が見えてきます。', '資料を統合する', 'formal', 'c2-unit-2'),
        ],
    ),
    PhrasebookCategory(
        id='rhetoric_ja_c2',
        level='C2',
        situation='修辞と批判的評価',
        icon='🧠',
        phrases=[
            _p('この表現は読者に強い印象を与えます。', '修辞効果を分析する', 'formal', 'c2-unit-4'),
            _p('主張自体は妥当ですが、根拠の示し方に課題があります。', '批判的に評価する', 'formal', 'c2-unit-7'),
            _p('反証を踏まえると、結論はより限定的に述べるべきです。', '反証を加味する', 'formal', 'c2-unit-7'),
            _p('文体を少し抑えることで、説得力が増します。', '編集方針を説明する', 'formal', 'c2-unit-6'),
        ],
    ),
    PhrasebookCategory(
        id='translation_mediation_ja_c2',
        level='C2',
        situation='翻訳と仲介',
        icon='🌐',
        phrases=[
            _p('この表現は直訳すると不自然になります。', '翻訳上の問題を説明する', 'formal', 'c2-unit-3'),
            _p('文脈に合わせて語調を調整する必要があります。', '語調調整を説明する', 'formal', 'c2-unit-3'),
            _p('原文の曖昧さをあえて残しています。', '翻訳方針を述べる', 'formal', 'c2-unit-3'),
            _p('専門用語は読者層に合わせて言い換えました。', '読者に合わせた調整を説明する', 'formal', 'c2-unit-3'),
            _p('この比喩は文化的背景を補う必要があります。', '文化差を説明する', 'formal', 'c2-unit-3'),
            _p('要点だけを抽出して伝えると、こうなります。', '仲介して要約する', 'formal', 'c2-unit-3'),
            _p('発言の意図を損なわないように訳しました。', '通訳判断を説明する', 'formal', 'c2-unit-3'),
            _p('二つの解釈が可能なので、補足が必要です。', '解釈の幅を示す', 'formal', 'c2-unit-3'),
        ],
    ),
    PhrasebookCategory(
        id='critical_review_ja_c2',
        level='C2',
        situation='批判的評価',
        icon='🧠',
        phrases=[
            _p('論点は明確ですが、根拠の提示が弱いです。', '論証を評価する', 'formal', 'c2-unit-7'),
            _p('前提そのものを問い直す必要があります。', '前提を批判する', 'formal', 'c2-unit-7'),
            _p('この反論は一部にしか当てはまりません。', '反論の範囲を限定する', 'formal', 'c2-unit-7'),
            _p('結論を支えるには追加の証拠が必要です。', '証拠不足を指摘する', 'formal', 'c2-unit-7'),
            _p('表現は巧みですが、論理に飛躍があります。', '文体と論理を分けて評価する', 'formal', 'c2-unit-4'),
            _p('別の価値観に立つと評価が変わります。', '評価基準を相対化する', 'formal', 'c2-unit-4'),
            _p('読者に与える印象も考慮すべきです。', '受け手への影響を述べる', 'formal', 'c2-unit-4'),
            _p('議論をより精密に組み立て直しましょう。', '改善を提案する', 'formal', 'c2-unit-7'),
        ],
    ),
    PhrasebookCategory(
        id='expert_explanation_ja_c2',
        level='C2',
        situation='専門的な説明',
        icon='🔬',
        phrases=[
            _p('専門外の方にも分かるように説明します。', '説明の方針を示す', 'formal', 'c2-unit-5'),
            _p('この概念は、簡単に言えば仕組みの土台です。', '概念を平易に説明する', 'formal', 'c2-unit-5'),
            _p('厳密には、二つの条件を区別する必要があります。', '厳密な区別を示す', 'formal', 'c2-unit-5'),
            _p('例外的なケースもありますが、原則は同じです。', '例外と原則を整理する', 'formal', 'c2-unit-5'),
            _p('因果関係と相関関係を混同しないことが重要です。', '専門的注意点を述べる', 'formal', 'c2-unit-5'),
            _p('このデータだけでは断定できません。', '限界を示す', 'formal', 'c2-unit-5'),
            _p('背景知識を補うと、理解しやすくなります。', '背景説明を加える', 'formal', 'c2-unit-5'),
            _p('結論を一文でまとめると、次の通りです。', '高度な内容を要約する', 'formal', 'c2-unit-5'),
        ],
    ),
    PhrasebookCategory(
        id='ethics_public_reasoning_ja_c2',
        level='C2',
        situation='倫理と公共的議論',
        icon='🏛️',
        phrases=[
            _p('公共性の観点から再検討する必要があります。', '公共性を論点にする', 'formal', 'c2-unit-7'),
            _p('透明性を確保しなければ信頼は得られません。', '透明性の重要性を述べる', 'formal', 'c2-unit-7'),
            _p('公平性と効率性の間に緊張関係があります。', '価値の衝突を説明する', 'formal', 'c2-unit-7'),
            _p('当事者の声を議論に組み込むべきです。', '当事者性を強調する', 'formal', 'c2-unit-7'),
            _p('その判断を正当化する根拠が問われます。', '正当化を求める', 'formal', 'c2-unit-7'),
            _p('短期的な成果と長期的な責任を分けて考えます。', '時間軸を分けて論じる', 'formal', 'c2-unit-7'),
            _p('合意形成には十分な説明が不可欠です。', '合意形成の条件を述べる', 'formal', 'c2-unit-6'),
            _p('価値判断を明示すると議論が整理されます。', '前提を明示する', 'formal', 'c2-unit-7'),
        ],
    ),
    PhrasebookCategory(
        id='advanced_synthesis_ja_c2',
        level='C2',
        situation='高度な統合と再構成',
        icon='🧩',
        phrases=[
            _p('複数の立場を統合すると、別の結論が導けます。', '複数視点を統合する', 'formal', 'c2-unit-7'),
            _p('この議論は用語の定義から見直す必要があります。', '定義から再検討する', 'formal', 'c2-unit-4'),
            _p('専門的な精度を保ちながら、表現を平易にします。', '精度と明快さを両立する', 'formal', 'c2-unit-5'),
            _p('原文の含意を損なわない範囲で再構成しました。', '含意を保って再構成する', 'formal', 'c2-unit-3'),
            _p('反対意見を組み込むことで、主張が強くなります。', '反対意見を統合する', 'formal', 'c2-unit-7'),
            _p('結論は断定せず、条件付きで提示するのが適切です。', '結論の強さを調整する', 'formal', 'c2-unit-7'),
        ],
    ),
]
