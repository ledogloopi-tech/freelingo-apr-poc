"""B2 phrasebook categories — Japanese (ja-JP)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry


def _p(text: str, context: str, register: str, unit_ref: str | None = None) -> PhrasebookEntry:
    return PhrasebookEntry(
        text=text,
        context=context,
        register=register,  # type: ignore[arg-type]
        unit_ref=unit_ref,
    )


B2_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="workplace_ja_b2",
        level="B2",
        situation="職場と敬語",
        icon="💼",
        phrases=[
            _p("資料をご確認いただけますでしょうか。", "資料確認を依頼する", "formal", "b2-unit-1"),
            _p("後ほど改めてご連絡いたします。", "連絡予定を伝える", "formal", "b2-unit-1"),
            _p("少々お待ちくださいませ。", "接客で待ってもらう", "formal", "b2-unit-1"),
            _p("担当者に確認いたします。", "確認することを伝える", "formal", "b2-unit-1"),
        ],
    ),
    PhrasebookCategory(
        id="argument_ja_b2",
        level="B2",
        situation="説明と論述",
        icon="📝",
        phrases=[
            _p("この点に関して、別の見方もあります。", "話題を導入する", "formal", "b2-unit-5"),
            _p("一方で、費用の問題も無視できません。", "対比する", "formal", "b2-unit-5"),
            _p("以上の理由から、改善が必要です。", "結論を述べる", "formal", "b2-unit-7"),
            _p("その可能性は低いかもしれません。", "控えめに推量する", "neutral", "b2-unit-6"),
        ],
    ),
    PhrasebookCategory(
        id="business_meetings_ja_b2",
        level="B2",
        situation="会議と調整",
        icon="💼",
        phrases=[
            _p("本日の議題を確認させてください。", "会議を始める", "formal", "b2-unit-1"),
            _p(
                "この点について補足してもよろしいでしょうか。",
                "補足を申し出る",
                "formal",
                "b2-unit-1",
            ),
            _p("優先順位を整理する必要があります。", "論点を整理する", "formal", "b2-unit-1"),
            _p("スケジュールを再調整しましょう。", "日程調整を提案する", "neutral", "b2-unit-1"),
            _p("関係部署に確認してから回答します。", "確認後の回答を伝える", "formal", "b2-unit-1"),
            _p("現時点では判断が難しいです。", "判断保留を伝える", "formal", "b2-unit-1"),
            _p("合意した内容を議事録に残します。", "合意内容を記録する", "formal", "b2-unit-1"),
            _p("次回までに代替案を用意します。", "次の対応を約束する", "formal", "b2-unit-1"),
        ],
    ),
    PhrasebookCategory(
        id="debate_ja_b2",
        level="B2",
        situation="討論と反論",
        icon="⚖️",
        phrases=[
            _p("その主張には一定の根拠があります。", "相手の論点を認める", "formal", "b2-unit-5"),
            _p("しかし、別の視点から見ると問題があります。", "反論を始める", "formal", "b2-unit-5"),
            _p("具体的なデータを見る必要があります。", "根拠を求める", "formal", "b2-unit-2"),
            _p(
                "この結論は少し飛躍していると思います。",
                "論理の弱点を指摘する",
                "neutral",
                "b2-unit-5",
            ),
            _p("前提が変われば、結果も変わります。", "条件を示す", "neutral", "b2-unit-5"),
            _p("短所だけでなく長所も考えるべきです。", "バランスを促す", "neutral", "b2-unit-5"),
            _p("私なら、別の方法を提案します。", "代替案を出す", "neutral", "b2-unit-5"),
            _p("ここまでの議論を整理しましょう。", "討論をまとめる", "formal", "b2-unit-5"),
        ],
    ),
    PhrasebookCategory(
        id="news_analysis_ja_b2",
        level="B2",
        situation="ニュース分析",
        icon="📰",
        phrases=[
            _p("この記事は背景説明が詳しいです。", "記事を評価する", "neutral", "b2-unit-2"),
            _p("見出しだけでは内容を判断できません。", "慎重な読解を促す", "neutral", "b2-unit-2"),
            _p(
                "専門家の意見も確認したほうがいいです。", "追加情報を求める", "neutral", "b2-unit-2"
            ),
            _p("統計の取り方に注意が必要です。", "データの扱いを指摘する", "formal", "b2-unit-2"),
            _p(
                "報道の仕方によって印象が変わります。",
                "メディア表現を分析する",
                "neutral",
                "b2-unit-2",
            ),
            _p("この問題は経済にも影響します。", "関連分野を示す", "neutral", "b2-unit-6"),
            _p("読者の反応は分かれています。", "世論を説明する", "neutral", "b2-unit-2"),
            _p("今後の展開を見守る必要があります。", "今後に言及する", "formal", "b2-unit-2"),
        ],
    ),
    PhrasebookCategory(
        id="project_management_ja_b2",
        level="B2",
        situation="プロジェクト進行",
        icon="📊",
        phrases=[
            _p("現在の進捗を共有します。", "進捗報告を始める", "formal", "b2-unit-1"),
            _p("この課題は優先度が高いです。", "優先度を示す", "formal", "b2-unit-1"),
            _p(
                "期限に間に合わせるには人員が必要です。",
                "リソース不足を伝える",
                "formal",
                "b2-unit-1",
            ),
            _p(
                "品質を保つために確認工程を増やします。",
                "品質管理を説明する",
                "formal",
                "b2-unit-1",
            ),
            _p("担当者を明確にしましょう。", "役割分担を促す", "neutral", "b2-unit-1"),
            _p("リスクを早めに共有してください。", "リスク共有を求める", "formal", "b2-unit-1"),
            _p("改善案を次回までにまとめます。", "次回アクションを伝える", "formal", "b2-unit-1"),
            _p("予定との差分を確認しましょう。", "計画との差を確認する", "neutral", "b2-unit-1"),
        ],
    ),
    PhrasebookCategory(
        id="professional_analysis_ja_b2",
        level="B2",
        situation="業務分析と提案",
        icon="📈",
        phrases=[
            _p(
                "現状を踏まえると、段階的な導入が現実的です。",
                "現実的な提案をする",
                "formal",
                "b2-unit-1",
            ),
            _p("費用対効果を確認してから判断しましょう。", "判断基準を示す", "formal", "b2-unit-6"),
            _p(
                "顧客への影響を最優先に考える必要があります。",
                "優先事項を述べる",
                "formal",
                "b2-unit-1",
            ),
            _p("この施策には短期的な効果が期待できます。", "効果を予測する", "formal", "b2-unit-6"),
            _p(
                "一方で、運用面の負担も増える可能性があります。",
                "懸念点を述べる",
                "formal",
                "b2-unit-5",
            ),
            _p("関係者の合意を得てから進めます。", "進行条件を伝える", "formal", "b2-unit-1"),
            _p("代替案を三つ比較してみました。", "比較結果を導入する", "formal", "b2-unit-5"),
            _p(
                "根拠となる資料を後ほど共有します。",
                "根拠資料の共有を伝える",
                "formal",
                "b2-unit-2",
            ),
            _p(
                "数字だけでなく利用者の声も重要です。",
                "定量と定性を対比する",
                "neutral",
                "b2-unit-2",
            ),
            _p(
                "この表現は少し強すぎるかもしれません。",
                "表現の強さを調整する",
                "neutral",
                "b2-unit-4",
            ),
            _p(
                "結論部分をもう少し明確にしましょう。", "文章改善を提案する", "neutral", "b2-unit-5"
            ),
            _p("次の会議で最終判断を行います。", "意思決定の予定を伝える", "formal", "b2-unit-1"),
        ],
    ),
]
