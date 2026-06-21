"""A2 phrasebook categories — Japanese (ja-JP)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry


def _p(text: str, context: str, register: str, unit_ref: str | None = None) -> PhrasebookEntry:
    return PhrasebookEntry(
        text=text,
        context=context,
        register=register,  # type: ignore[arg-type]
        unit_ref=unit_ref,
    )


A2_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="travel_ja_a2",
        level="A2",
        situation="旅行と予約",
        icon="🧳",
        phrases=[
            _p("予約を確認したいです。", "ホテルや店で予約を確認する", "formal", "a2-unit-1"),
            _p("駅までどう行けばいいですか。", "道順を尋ねる", "neutral", "a2-unit-1"),
            _p("写真を撮ってもいいですか。", "許可を求める", "neutral", "a2-unit-2"),
            _p(
                "どちらがおすすめですか。",
                "二つの選択肢からおすすめを尋ねる",
                "neutral",
                "a2-unit-4",
            ),
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
        id="transport_ja_a2",
        level="A2",
        situation="交通機関",
        icon="🚆",
        phrases=[
            _p("この電車は東京駅に行きますか。", "行き先を確認する", "neutral", "a2-unit-1"),
            _p("次の電車は何時ですか。", "時刻を尋ねる", "neutral", "a2-unit-1"),
            _p("どこで乗り換えればいいですか。", "乗り換えを尋ねる", "neutral", "a2-unit-1"),
            _p("片道切符を一枚ください。", "切符を買う", "neutral", "a2-unit-1"),
            _p("遅延していますか。", "遅れを確認する", "formal", "a2-unit-1"),
            _p("この席は空いていますか。", "座席を確認する", "neutral", "a2-unit-1"),
            _p("出口はどちらですか。", "出口を尋ねる", "formal", "a2-unit-1"),
            _p("タクシー乗り場はどこですか。", "乗り場を尋ねる", "neutral", "a2-unit-1"),
        ],
    ),
    PhrasebookCategory(
        id="appointments_ja_a2",
        level="A2",
        situation="予約と予定変更",
        icon="📅",
        phrases=[
            _p("明日の予約を取りたいです。", "予約を取る", "formal", "a2-unit-3"),
            _p("予約を変更できますか。", "予定変更を依頼する", "formal", "a2-unit-3"),
            _p("三時は空いていますか。", "空き時間を確認する", "neutral", "a2-unit-3"),
            _p("少し遅れます。", "遅刻を伝える", "neutral", "a2-unit-3"),
            _p("キャンセルしたいです。", "予約を取り消す", "formal", "a2-unit-3"),
            _p("確認メールを送ってください。", "確認を依頼する", "formal", "a2-unit-3"),
            _p("来週の同じ時間でお願いします。", "次回予定を決める", "formal", "a2-unit-3"),
            _p("都合が悪くなりました。", "予定変更の理由を伝える", "neutral", "a2-unit-3"),
        ],
    ),
    PhrasebookCategory(
        id="problems_ja_a2",
        level="A2",
        situation="困った時",
        icon="🆘",
        phrases=[
            _p("道に迷いました。", "迷子になったことを伝える", "neutral", "a2-unit-1"),
            _p("財布をなくしました。", "紛失を伝える", "neutral", "a2-unit-2"),
            _p("警察に連絡したほうがいいですか。", "助言を求める", "neutral", "a2-unit-7"),
            _p("ここで待っていてもいいですか。", "許可を求める", "neutral", "a2-unit-2"),
            _p("日本語がまだ上手ではありません。", "言語力を説明する", "neutral", "a2-unit-6"),
            _p("英語で説明できますか。", "別言語での説明を依頼する", "neutral", "a2-unit-6"),
            _p("もう少し簡単に言ってください。", "易しい説明を頼む", "formal", "a2-unit-6"),
            _p("助けてくれてありがとうございます。", "感謝を伝える", "neutral", "a2-unit-7"),
        ],
    ),
    PhrasebookCategory(
        id="forms_services_ja_a2",
        level="A2",
        situation="窓口と手続き",
        icon="🧾",
        phrases=[
            _p("この用紙に記入すればいいですか。", "記入方法を確認する", "formal", "a2-unit-4"),
            _p("身分証明書が必要ですか。", "必要書類を尋ねる", "formal", "a2-unit-4"),
            _p("番号札を取って待てばいいですか。", "順番待ちを確認する", "formal", "a2-unit-4"),
            _p("手数料はいくらですか。", "料金を尋ねる", "neutral", "a2-unit-4"),
            _p("今日中に受け取れますか。", "受け取り時期を確認する", "neutral", "a2-unit-4"),
            _p("住所を変更したいです。", "変更手続きを依頼する", "formal", "a2-unit-4"),
            _p("コピーは必要ですか。", "追加書類を確認する", "neutral", "a2-unit-4"),
            _p("どこに提出すればいいですか。", "提出場所を尋ねる", "formal", "a2-unit-4"),
        ],
    ),
    PhrasebookCategory(
        id="daily_services_ja_a2",
        level="A2",
        situation="日常サービスと相談",
        icon="🏪",
        phrases=[
            _p("この商品を返品したいです。", "返品を依頼する", "formal", "a2-unit-4"),
            _p("別のサイズはありますか。", "サイズ違いを尋ねる", "neutral", "a2-unit-4"),
            _p("試着してもいいですか。", "試着の許可を求める", "neutral", "a2-unit-4"),
            _p("領収書をいただけますか。", "領収書を頼む", "formal", "a2-unit-4"),
            _p("部屋の電気がつきません。", "設備の故障を伝える", "neutral", "a2-unit-2"),
            _p("修理をお願いできますか。", "修理を依頼する", "formal", "a2-unit-2"),
            _p("明日までに必要です。", "期限を伝える", "neutral", "a2-unit-3"),
            _p("時間を変更してもらえますか。", "時間変更を頼む", "formal", "a2-unit-3"),
            _p("参加費はいくらですか。", "参加費を尋ねる", "neutral", "a2-unit-3"),
            _p(
                "友だちを連れて行ってもいいですか。", "同行者の許可を求める", "neutral", "a2-unit-3"
            ),
            _p("この薬は一日何回飲みますか。", "薬の飲み方を尋ねる", "neutral", "a2-unit-5"),
            _p("保険証を忘れました。", "忘れ物を伝える", "neutral", "a2-unit-5"),
            _p("もう少し詳しく説明してください。", "詳しい説明を求める", "formal", "a2-unit-6"),
            _p("確認してから連絡します。", "後で連絡することを伝える", "formal", "a2-unit-6"),
        ],
    ),
]
