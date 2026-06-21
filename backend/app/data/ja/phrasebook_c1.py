"""C1 phrasebook categories — Japanese (ja-JP)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry


def _p(text: str, context: str, register: str, unit_ref: str | None = None) -> PhrasebookEntry:
    return PhrasebookEntry(
        text=text,
        context=context,
        register=register,  # type: ignore[arg-type]
        unit_ref=unit_ref,
    )


C1_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="negotiation_ja_c1",
        level="C1",
        situation="交渉と婉曲表現",
        icon="🗣️",
        phrases=[
            _p(
                "大変恐縮ですが、条件を再検討いただけないでしょうか。",
                "丁寧に再検討を依頼する",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "その点については、やや慎重に考える必要があります。",
                "直接的すぎず懸念を伝える",
                "formal",
                "c1-unit-4",
            ),
            _p("ご提案の趣旨は理解しております。", "相手の立場を受け止める", "formal", "c1-unit-4"),
            _p("代替案として、次の方法が考えられます。", "代替案を出す", "formal", "c1-unit-4"),
        ],
    ),
    PhrasebookCategory(
        id="presentation_ja_c1",
        level="C1",
        situation="発表と討論",
        icon="🎙️",
        phrases=[
            _p("本日は三つの観点からお話しします。", "発表を始める", "formal", "c1-unit-6"),
            _p(
                "ここで重要なのは、原因と結果を分けて考えることです。",
                "論点を整理する",
                "formal",
                "c1-unit-6",
            ),
            _p("ご質問の点について補足します。", "質問に答える", "formal", "c1-unit-6"),
            _p("結論として、段階的な対応が必要です。", "結論を述べる", "formal", "c1-unit-6"),
        ],
    ),
    PhrasebookCategory(
        id="negotiation_extended_ja_c1",
        level="C1",
        situation="高度な交渉",
        icon="🤝",
        phrases=[
            _p(
                "双方にとって現実的な落としどころを探りたいです。",
                "妥協点を探る",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "ご懸念は理解しておりますが、別案も検討可能です。",
                "懸念を受け止める",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "この条件であれば、社内で前向きに検討できます。",
                "条件付きで受け入れる",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "結論を出す前に、前提を確認させてください。",
                "前提確認を求める",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "短期的な利益だけで判断するのは避けたいです。",
                "慎重な姿勢を示す",
                "formal",
                "c1-unit-3",
            ),
            _p(
                "責任範囲を明確にしておく必要があります。",
                "責任分担を確認する",
                "formal",
                "c1-unit-3",
            ),
            _p("本件については持ち帰って検討いたします。", "即答を避ける", "formal", "c1-unit-4"),
            _p("合意内容を書面で確認できれば安心です。", "書面確認を求める", "formal", "c1-unit-5"),
        ],
    ),
    PhrasebookCategory(
        id="academic_discussion_ja_c1",
        level="C1",
        situation="学術的な議論",
        icon="🎓",
        phrases=[
            _p(
                "この研究の目的は、原因を明らかにすることです。",
                "研究目的を述べる",
                "formal",
                "c1-unit-1",
            ),
            _p("先行研究では十分に扱われていません。", "研究ギャップを示す", "formal", "c1-unit-1"),
            _p("調査方法にはいくつかの制約があります。", "限界を認める", "formal", "c1-unit-1"),
            _p("この結果は仮説を支持しています。", "結果を解釈する", "formal", "c1-unit-1"),
            _p("別の解釈も成り立つ可能性があります。", "代替解釈を示す", "formal", "c1-unit-1"),
            _p("用語をここで定義しておきます。", "定義を提示する", "formal", "c1-unit-1"),
            _p(
                "質的データと量的データを組み合わせました。",
                "方法を説明する",
                "formal",
                "c1-unit-1",
            ),
            _p(
                "今後の課題として、対象を広げる必要があります。",
                "今後の課題を述べる",
                "formal",
                "c1-unit-1",
            ),
        ],
    ),
    PhrasebookCategory(
        id="formal_writing_ja_c1",
        level="C1",
        situation="フォーマルな文章",
        icon="✉️",
        phrases=[
            _p(
                "平素より大変お世話になっております。",
                "ビジネスメールの冒頭",
                "formal",
                "c1-unit-5",
            ),
            _p(
                "ご多忙のところ恐縮ですが、ご確認ください。",
                "確認を依頼する",
                "formal",
                "c1-unit-5",
            ),
            _p(
                "詳細につきましては、添付資料をご参照ください。",
                "資料を案内する",
                "formal",
                "c1-unit-5",
            ),
            _p(
                "ご不明な点がございましたら、お知らせください。",
                "問い合わせを促す",
                "formal",
                "c1-unit-5",
            ),
            _p("ご期待に沿えず申し訳ございません。", "丁寧に断る", "formal", "c1-unit-4"),
            _p("何卒よろしくお願い申し上げます。", "メールを締める", "formal", "c1-unit-5"),
            _p("取り急ぎ、ご報告まで。", "短い報告を締める", "formal", "c1-unit-5"),
            _p("後日改めてご連絡差し上げます。", "後続連絡を伝える", "formal", "c1-unit-5"),
        ],
    ),
    PhrasebookCategory(
        id="register_control_ja_c1",
        level="C1",
        situation="待遇表現の調整",
        icon="🎚️",
        phrases=[
            _p(
                "この場面では少し丁寧すぎるかもしれません。",
                "敬語の過剰さを指摘する",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "相手との距離感に合わせて表現を変えましょう。",
                "待遇を調整する",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "社外向けなら、こちらの言い回しが自然です。",
                "場面に合う表現を提案する",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "断定を避けることで柔らかい印象になります。",
                "婉曲表現を説明する",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "この表現はややくだけた印象があります。",
                "レジスターを評価する",
                "formal",
                "c1-unit-4",
            ),
            _p("敬意は保ちつつ、文を短くできます。", "自然な敬語を提案する", "formal", "c1-unit-4"),
            _p(
                "謝意を先に示すと受け入れられやすいです。",
                "配慮の順序を説明する",
                "formal",
                "c1-unit-4",
            ),
            _p(
                "この言い方なら押しつけがましく聞こえません。",
                "柔らかい提案を示す",
                "formal",
                "c1-unit-4",
            ),
        ],
    ),
    PhrasebookCategory(
        id="executive_summary_ja_c1",
        level="C1",
        situation="要約と意思決定",
        icon="📌",
        phrases=[
            _p("要するに、課題は実行体制にあります。", "核心を要約する", "formal", "c1-unit-3"),
            _p(
                "判断材料がそろった段階で結論を出しましょう。",
                "意思決定の条件を示す",
                "formal",
                "c1-unit-3",
            ),
            _p(
                "この選択肢は妥当ですが、リスク管理が必要です。",
                "選択肢を評価する",
                "formal",
                "c1-unit-3",
            ),
            _p(
                "論点を三つに絞ると議論しやすくなります。",
                "論点整理を提案する",
                "formal",
                "c1-unit-6",
            ),
            _p(
                "相手の意図をくみ取った上で返答します。",
                "配慮した応答を説明する",
                "formal",
                "c1-unit-4",
            ),
        ],
    ),
]
