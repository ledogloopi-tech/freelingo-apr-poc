"""B1 phrasebook categories — Japanese (ja-JP)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry


def _p(text: str, context: str, register: str, unit_ref: str | None = None) -> PhrasebookEntry:
    return PhrasebookEntry(
        text=text,
        context=context,
        register=register,  # type: ignore[arg-type]
        unit_ref=unit_ref,
    )


B1_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="opinions_ja_b1",
        level="B1",
        situation="意見交換",
        icon="💬",
        phrases=[
            _p("私は少し違う意見です。", "丁寧に反対する", "neutral", "b1-unit-7"),
            _p("その理由は二つあります。", "理由を整理して述べる", "neutral", "b1-unit-7"),
            _p("例えば、地域の活動が増えています。", "例を挙げる", "neutral", "b1-unit-7"),
            _p("つまり、準備が大切だということです。", "要点をまとめる", "neutral", "b1-unit-1"),
        ],
    ),
    PhrasebookCategory(
        id="helping_ja_b1",
        level="B1",
        situation="手助けと授受",
        icon="🤝",
        phrases=[
            _p("友だちが手伝ってくれました。", "助けてもらったことを話す", "neutral", "b1-unit-4"),
            _p("資料を送っていただけますか。", "丁寧に依頼する", "formal", "b1-unit-4"),
            _p("私が説明しましょうか。", "申し出る", "neutral", "b1-unit-4"),
            _p("助けてくださってありがとうございます。", "丁寧に感謝する", "formal", "b1-unit-4"),
        ],
    ),
    PhrasebookCategory(
        id="opinions_extended_ja_b1",
        level="B1",
        situation="意見と理由",
        icon="💬",
        phrases=[
            _p("私の考えでは、まず情報を集めるべきです。", "意見を述べる", "neutral", "b1-unit-7"),
            _p(
                "その点には賛成ですが、別の問題もあります。",
                "部分的に同意する",
                "neutral",
                "b1-unit-7",
            ),
            _p("理由をもう少し詳しく説明してもらえますか。", "理由を求める", "formal", "b1-unit-7"),
            _p("具体的な例を挙げると分かりやすいです。", "例を求める", "neutral", "b1-unit-7"),
            _p("一番大きな理由は費用だと思います。", "主要因を示す", "neutral", "b1-unit-7"),
            _p(
                "短期的には便利ですが、長期的には心配です。",
                "対比して評価する",
                "neutral",
                "b1-unit-7",
            ),
            _p("この方法なら多くの人が参加できます。", "利点を説明する", "neutral", "b1-unit-7"),
            _p(
                "結論を急がないほうがいいと思います。", "慎重な意見を述べる", "neutral", "b1-unit-7"
            ),
        ],
    ),
    PhrasebookCategory(
        id="work_study_ja_b1",
        level="B1",
        situation="仕事と学習",
        icon="📚",
        phrases=[
            _p("課題の締め切りを確認したいです。", "締め切りを確認する", "formal", "b1-unit-2"),
            _p("資料を共有していただけますか。", "資料共有を依頼する", "formal", "b1-unit-2"),
            _p("発表の準備はほとんど終わりました。", "進捗を伝える", "neutral", "b1-unit-2"),
            _p("この部分について質問があります。", "質問を切り出す", "neutral", "b1-unit-2"),
            _p("先に要点をまとめます。", "説明を始める", "neutral", "b1-unit-2"),
            _p("もう一度確認してから提出します。", "確認予定を伝える", "formal", "b1-unit-2"),
            _p("チームで役割を分けましょう。", "作業分担を提案する", "neutral", "b1-unit-4"),
            _p("ご意見を参考にします。", "意見への感謝を示す", "formal", "b1-unit-7"),
        ],
    ),
    PhrasebookCategory(
        id="community_ja_b1",
        level="B1",
        situation="地域と社会生活",
        icon="🏙️",
        phrases=[
            _p(
                "地域のイベントに参加してみたいです。",
                "地域活動への関心を示す",
                "neutral",
                "b1-unit-1",
            ),
            _p("この施設は誰でも利用できますか。", "利用条件を尋ねる", "neutral", "b1-unit-1"),
            _p("ごみの分別方法を教えてください。", "生活ルールを尋ねる", "formal", "b1-unit-5"),
            _p("近所の人ともっと交流したいです。", "交流の希望を伝える", "neutral", "b1-unit-1"),
            _p("防災訓練はいつ行われますか。", "地域予定を確認する", "formal", "b1-unit-1"),
            _p(
                "この問題について住民の意見を聞くべきです。",
                "地域課題への意見を述べる",
                "neutral",
                "b1-unit-7",
            ),
            _p("安全のためにルールを守りましょう。", "注意を促す", "neutral", "b1-unit-5"),
            _p("困った時は窓口に相談できます。", "相談先を案内する", "neutral", "b1-unit-4"),
        ],
    ),
    PhrasebookCategory(
        id="career_interview_ja_b1",
        level="B1",
        situation="面接とキャリア",
        icon="🧑\u200d💼",
        phrases=[
            _p("これまで接客の経験があります。", "経験を説明する", "formal", "b1-unit-6"),
            _p("チームで働くことが得意です。", "強みを伝える", "formal", "b1-unit-6"),
            _p("新しい仕事に挑戦したいです。", "志望理由を伝える", "formal", "b1-unit-6"),
            _p("勤務時間について質問があります。", "条件を尋ねる", "formal", "b1-unit-6"),
            _p("研修制度はありますか。", "研修について尋ねる", "formal", "b1-unit-6"),
            _p("将来は管理の仕事にも関わりたいです。", "将来目標を述べる", "formal", "b1-unit-6"),
            _p(
                "前職では資料作成を担当していました。",
                "過去の担当を説明する",
                "formal",
                "b1-unit-6",
            ),
            _p(
                "本日はお時間をいただきありがとうございます。",
                "面接で感謝する",
                "formal",
                "b1-unit-6",
            ),
        ],
    ),
    PhrasebookCategory(
        id="daily_discussion_ja_b1",
        level="B1",
        situation="日常の説明と相談",
        icon="🗨️",
        phrases=[
            _p("最近、生活のリズムが少し変わりました。", "近況を説明する", "neutral", "b1-unit-1"),
            _p(
                "その経験から多くのことを学びました。",
                "経験から得た学びを話す",
                "neutral",
                "b1-unit-2",
            ),
            _p("以前より日本語で話す自信がつきました。", "成長を述べる", "neutral", "b1-unit-2"),
            _p(
                "予定が合えば、ぜひ参加したいです。",
                "条件付きで参加を伝える",
                "neutral",
                "b1-unit-3",
            ),
            _p(
                "急な用事ができたので、少し遅れます。", "遅刻理由を説明する", "neutral", "b1-unit-3"
            ),
            _p(
                "その件について、後で相談してもいいですか。",
                "後で相談を依頼する",
                "formal",
                "b1-unit-4",
            ),
            _p("相手の立場も考える必要があります。", "配慮を示す", "neutral", "b1-unit-4"),
            _p(
                "環境のためにできることから始めたいです。",
                "環境への姿勢を述べる",
                "neutral",
                "b1-unit-5",
            ),
            _p(
                "このサービスは使いやすいと思います。", "サービスを評価する", "neutral", "b1-unit-6"
            ),
            _p("安全面ではまだ改善が必要です。", "改善点を述べる", "neutral", "b1-unit-5"),
            _p("その説明でだいたい理解できました。", "理解度を伝える", "neutral", "b1-unit-2"),
            _p("もう少し時間をかけて考えたいです。", "判断を保留する", "neutral", "b1-unit-7"),
            _p("私も同じような経験があります。", "共通経験を示す", "neutral", "b1-unit-4"),
            _p(
                "状況によって答えが変わると思います。",
                "条件による違いを述べる",
                "neutral",
                "b1-unit-7",
            ),
            _p("問題を小さく分けて考えましょう。", "整理を提案する", "neutral", "b1-unit-7"),
            _p("最後に要点を確認しておきます。", "要点確認を始める", "formal", "b1-unit-7"),
        ],
    ),
]
