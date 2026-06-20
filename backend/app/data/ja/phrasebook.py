"""Japanese phrasebook data."""

from app.data._types import PhrasebookCategory, PhrasebookEntry


def _p(text: str, context: str, register: str, unit_ref: str | None = None) -> PhrasebookEntry:
    return PhrasebookEntry(
        text=text,
        context=context,
        register=register,  # type: ignore[arg-type]
        unit_ref=unit_ref,
    )


PHRASEBOOK_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="greetings_ja_a1",
        level="A1",
        situation="あいさつと自己紹介",
        icon="👋",
        phrases=[
            _p("はじめまして。", "初対面のあいさつ", "neutral", "a1-unit-1"),
            _p("よろしくお願いします。", "自己紹介の締めくくり", "formal", "a1-unit-1"),
            _p("お名前は何ですか。", "相手の名前を尋ねる", "neutral", "a1-unit-2"),
            _p("スペインから来ました。", "出身を伝える", "neutral", "a1-unit-2"),
        ],
    ),
    PhrasebookCategory(
        id="classroom_ja_a1",
        level="A1",
        situation="教室で使う表現",
        icon="📚",
        phrases=[
            _p("もう一度お願いします。", "聞き返す", "formal", "a1-unit-7"),
            _p("ゆっくり話してください。", "話す速度を調整してもらう", "formal", "a1-unit-7"),
            _p("これはどういう意味ですか。", "意味を尋ねる", "neutral", "a1-unit-1"),
            _p("分かりました。", "理解したことを伝える", "neutral", "a1-unit-1"),
        ],
    ),
    PhrasebookCategory(
        id="shopping_ja_a1",
        level="A1",
        situation="買い物",
        icon="🛍️",
        phrases=[
            _p("これはいくらですか。", "値段を尋ねる", "neutral", "a1-unit-7"),
            _p("これをください。", "商品を選んで頼む", "neutral", "a1-unit-7"),
            _p("袋をお願いします。", "袋を頼む", "formal", "a1-unit-7"),
            _p("カードで払えますか。", "支払い方法を確認する", "neutral", "a1-unit-7"),
        ],
    ),
    PhrasebookCategory(
        id="travel_ja_a2",
        level="A2",
        situation="旅行と予約",
        icon="🧳",
        phrases=[
            _p("予約を確認したいです。", "ホテルや店で予約を確認する", "formal", "a2-unit-1"),
            _p("駅までどう行けばいいですか。", "道順を尋ねる", "neutral", "a2-unit-1"),
            _p("写真を撮ってもいいですか。", "許可を求める", "neutral", "a2-unit-2"),
            _p("おすすめは何ですか。", "おすすめを尋ねる", "neutral", "a2-unit-4"),
        ],
    ),
    PhrasebookCategory(
        id="health_ja_a2",
        level="A2",
        situation="体調と助言",
        icon="🏥",
        phrases=[
            _p("頭が痛いです。", "症状を伝える", "neutral", "a2-unit-5"),
            _p("病院に行ったほうがいいです。", "助言する", "neutral", "a2-unit-7"),
            _p("薬を飲まなければなりません。", "必要な行動を伝える", "neutral", "a2-unit-7"),
            _p("ここで電話してはいけません。", "禁止を伝える", "neutral", "a2-unit-7"),
        ],
    ),
    PhrasebookCategory(
        id="plans_ja_a2",
        level="A2",
        situation="予定と希望",
        icon="📅",
        phrases=[
            _p("週末に京都へ行くつもりです。", "自分の予定を伝える", "neutral", "a2-unit-3"),
            _p("日本語をもっと話せるようになりたいです。", "目標を伝える", "neutral", "a2-unit-3"),
            _p("来週、会議の予定があります。", "決まった予定を伝える", "formal", "a2-unit-3"),
            _p("今日は早く帰りたいです。", "希望を伝える", "neutral", "a2-unit-3"),
        ],
    ),
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
        id="mediation_ja_c2",
        level="C2",
        situation="仲介と専門説明",
        icon="🌐",
        phrases=[
            _p(
                "専門用語を避けて言い換えると、次のようになります。",
                "分かりやすく言い換える",
                "formal",
                "c2-unit-3",
            ),
            _p(
                "原文のニュアンスを保つなら、この表現が近いです。",
                "翻訳の選択を説明する",
                "formal",
                "c2-unit-3",
            ),
            _p(
                "この議論の前提には、二つの価値判断があります。",
                "前提を分析する",
                "formal",
                "c2-unit-7",
            ),
            _p(
                "複数の資料を照合すると、異なる結論が見えてきます。",
                "資料を統合する",
                "formal",
                "c2-unit-2",
            ),
        ],
    ),
    PhrasebookCategory(
        id="rhetoric_ja_c2",
        level="C2",
        situation="修辞と批判的評価",
        icon="🧠",
        phrases=[
            _p("この表現は読者に強い印象を与えます。", "修辞効果を分析する", "formal", "c2-unit-4"),
            _p(
                "主張自体は妥当ですが、根拠の示し方に課題があります。",
                "批判的に評価する",
                "formal",
                "c2-unit-7",
            ),
            _p(
                "反証を踏まえると、結論はより限定的に述べるべきです。",
                "反証を加味する",
                "formal",
                "c2-unit-7",
            ),
            _p(
                "文体を少し抑えることで、説得力が増します。",
                "編集方針を説明する",
                "formal",
                "c2-unit-6",
            ),
        ],
    ),
]
