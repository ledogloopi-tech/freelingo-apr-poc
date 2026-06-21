"""A1 phrasebook categories — Japanese (ja-JP)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry


def _p(text: str, context: str, register: str, unit_ref: str | None = None) -> PhrasebookEntry:
    return PhrasebookEntry(
        text=text,
        context=context,
        register=register,  # type: ignore[arg-type]
        unit_ref=unit_ref,
    )


A1_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id='greetings_ja_a1',
        level='A1',
        situation='あいさつと自己紹介',
        icon='👋',
        phrases=[
            _p('はじめまして。', '初対面のあいさつ', 'neutral', 'a1-unit-1'),
            _p('よろしくお願いします。', '自己紹介の締めくくり', 'formal', 'a1-unit-1'),
            _p('お名前は何ですか。', '相手の名前を尋ねる', 'neutral', 'a1-unit-2'),
            _p('スペインから来ました。', '出身を伝える', 'neutral', 'a1-unit-2'),
        ],
    ),
    PhrasebookCategory(
        id='classroom_ja_a1',
        level='A1',
        situation='教室で使う表現',
        icon='📚',
        phrases=[
            _p('もう一度お願いします。', '聞き返す', 'formal', 'a1-unit-7'),
            _p('ゆっくり話してください。', '話す速度を調整してもらう', 'formal', 'a1-unit-7'),
            _p('これはどういう意味ですか。', '意味を尋ねる', 'neutral', 'a1-unit-1'),
            _p('分かりました。', '理解したことを伝える', 'neutral', 'a1-unit-1'),
        ],
    ),
    PhrasebookCategory(
        id='shopping_ja_a1',
        level='A1',
        situation='買い物',
        icon='🛍️',
        phrases=[
            _p('これはいくらですか。', '値段を尋ねる', 'neutral', 'a1-unit-7'),
            _p('これをください。', '商品を選んで頼む', 'neutral', 'a1-unit-7'),
            _p('袋をお願いします。', '袋を頼む', 'formal', 'a1-unit-7'),
            _p('カードで払えますか。', '支払い方法を確認する', 'neutral', 'a1-unit-7'),
        ],
    ),
    PhrasebookCategory(
        id='daily_requests_ja_a1',
        level='A1',
        situation='日常の依頼',
        icon='🙋',
        phrases=[
            _p('すみません、お願いします。', '丁寧に依頼を始める', 'formal', 'a1-unit-1'),
            _p('もう一度言ってください。', '聞き返す', 'formal', 'a1-unit-1'),
            _p('少し待ってください。', '待ってもらう', 'formal', 'a1-unit-4'),
            _p('これを見てください。', '相手に物を見せる', 'neutral', 'a1-unit-4'),
            _p('ここに書いてください。', '記入を頼む', 'formal', 'a1-unit-4'),
            _p('手伝ってください。', '助けを求める', 'formal', 'a1-unit-4'),
            _p('写真をお願いします。', '写真撮影を頼む', 'formal', 'a1-unit-6'),
            _p('水をください。', '飲み物を頼む', 'neutral', 'a1-unit-5'),
        ],
    ),
    PhrasebookCategory(
        id='restaurant_ja_a1',
        level='A1',
        situation='レストラン',
        icon='🍜',
        phrases=[
            _p('二人です。', '人数を伝える', 'neutral', 'a1-unit-5'),
            _p('メニューをお願いします。', 'メニューを頼む', 'formal', 'a1-unit-5'),
            _p('おすすめは何ですか。', 'おすすめを尋ねる', 'neutral', 'a1-unit-5'),
            _p('これを一つください。', '注文する', 'neutral', 'a1-unit-5'),
            _p('辛くないですか。', '味を確認する', 'neutral', 'a1-unit-5'),
            _p('とてもおいしいです。', '感想を言う', 'neutral', 'a1-unit-5'),
            _p('お会計をお願いします。', '会計を頼む', 'formal', 'a1-unit-5'),
            _p('別々に払えますか。', '支払い方法を確認する', 'neutral', 'a1-unit-7'),
        ],
    ),
    PhrasebookCategory(
        id='directions_ja_a1',
        level='A1',
        situation='道案内',
        icon='🗺️',
        phrases=[
            _p('駅はどこですか。', '場所を尋ねる', 'neutral', 'a1-unit-6'),
            _p('ここから近いですか。', '距離を確認する', 'neutral', 'a1-unit-6'),
            _p('まっすぐ行ってください。', '直進を伝える', 'neutral', 'a1-unit-6'),
            _p('右に曲がってください。', '右折を伝える', 'neutral', 'a1-unit-6'),
            _p('左に曲がってください。', '左折を伝える', 'neutral', 'a1-unit-6'),
            _p('この地図を見てください。', '地図で説明する', 'neutral', 'a1-unit-6'),
            _p('歩いて十分ぐらいです。', '所要時間を伝える', 'neutral', 'a1-unit-6'),
            _p('ありがとうございます、助かりました。', '道案内に感謝する', 'formal', 'a1-unit-6'),
        ],
    ),
    PhrasebookCategory(
        id='family_smalltalk_ja_a1',
        level='A1',
        situation='家族と雑談',
        icon='👨\u200d👩\u200d👧',
        phrases=[
            _p('ご家族は何人ですか。', '家族について尋ねる', 'neutral', 'a1-unit-2'),
            _p('兄が一人います。', '兄弟について話す', 'neutral', 'a1-unit-2'),
            _p('週末は家にいます。', '週末の予定を話す', 'neutral', 'a1-unit-8'),
            _p('今日はいい天気ですね。', '天気の雑談をする', 'neutral', 'a1-unit-8'),
            _p('少し暑いですね。', '気候について話す', 'neutral', 'a1-unit-8'),
            _p('この近くに住んでいます。', '住んでいる場所を話す', 'neutral', 'a1-unit-6'),
            _p('日本語を勉強しています。', '学習中であることを伝える', 'neutral', 'a1-unit-1'),
            _p('どうぞよろしく。', 'カジュアルに締める', 'informal', 'a1-unit-1'),
        ],
    ),
    PhrasebookCategory(
        id='daily_survival_ja_a1',
        level='A1',
        situation='生活の基本表現',
        icon='🏠',
        phrases=[
            _p('トイレはどこですか。', '必要な場所を尋ねる', 'neutral', 'a1-unit-6'),
            _p('ここに座ってもいいですか。', '許可を求める', 'neutral', 'a1-unit-4'),
            _p('これは私の席です。', '自分の席を示す', 'neutral', 'a1-unit-3'),
            _p('すみません、分かりません。', '理解できないことを伝える', 'neutral', 'a1-unit-1'),
            _p('日本語で何と言いますか。', '言い方を尋ねる', 'neutral', 'a1-unit-1'),
            _p('ゆっくりお願いします。', 'ゆっくり話してもらう', 'formal', 'a1-unit-1'),
            _p('今、何時ですか。', '時間を尋ねる', 'neutral', 'a1-unit-3'),
            _p('今日は何曜日ですか。', '曜日を尋ねる', 'neutral', 'a1-unit-3'),
            _p('これは誰のかばんですか。', '持ち主を尋ねる', 'neutral', 'a1-unit-3'),
            _p('私の電話番号です。', '電話番号を伝える', 'neutral', 'a1-unit-2'),
            _p('少し寒いです。', '体感を伝える', 'neutral', 'a1-unit-8'),
            _p('窓を開けてもいいですか。', '窓を開ける許可を求める', 'neutral', 'a1-unit-4'),
            _p('写真を見せてください。', '写真を見せてもらう', 'formal', 'a1-unit-4'),
            _p('一緒に行きましょう。', '誘う', 'neutral', 'a1-unit-6'),
            _p('また明日会いましょう。', '次に会う予定を言う', 'neutral', 'a1-unit-8'),
            _p('気をつけてください。', '注意を促す', 'formal', 'a1-unit-8'),
            _p('お疲れさまでした。', '活動の終わりに声をかける', 'neutral', 'a1-unit-8'),
        ],
    ),
]
