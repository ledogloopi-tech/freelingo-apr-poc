"""A1 phrasebook categories — Korean (ko-KR)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry

A1_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="greetings_a1",
        level="A1",
        situation="인사와 소개",
        icon="👋",
        phrases=[
            PhrasebookEntry(
                text="안녕하세요.",
                context="처음 만나거나 공손하게 인사할 때",
                register="formal",
                unit_ref="a1-unit-1",
            ),
            PhrasebookEntry(
                text="저는 민수예요.",
                context="이름을 소개할 때",
                register="neutral",
                unit_ref="a1-unit-1",
            ),
            PhrasebookEntry(
                text="만나서 반가워요.",
                context="처음 만난 사람에게 말할 때",
                register="neutral",
                unit_ref="a1-unit-1",
            ),
        ],
    ),
    PhrasebookCategory(
        id="classroom_a1",
        level="A1",
        situation="교실 표현",
        icon="📚",
        phrases=[
            PhrasebookEntry(
                text="다시 말씀해 주세요.",
                context="말을 다시 듣고 싶을 때",
                register="formal",
                unit_ref="a1-unit-1",
            ),
            PhrasebookEntry(
                text="질문이 있어요.",
                context="수업 중 질문할 때",
                register="neutral",
                unit_ref="a1-unit-1",
            ),
            PhrasebookEntry(
                text="잘 모르겠어요.",
                context="이해하지 못했을 때",
                register="neutral",
                unit_ref="a1-unit-1",
            ),
        ],
    ),
    PhrasebookCategory(
        id="identity_a1",
        level="A1",
        situation="자기소개",
        icon="🪪",
        phrases=[
            PhrasebookEntry(
                text="저는 스페인에서 왔어요.",
                context="출신을 말할 때",
                register="neutral",
                unit_ref="a1-unit-2",
            ),
            PhrasebookEntry(
                text="직업은 회사원이에요.",
                context="직업을 소개할 때",
                register="neutral",
                unit_ref="a1-unit-2",
            ),
            PhrasebookEntry(
                text="한국어를 공부해요.",
                context="학습 목적을 말할 때",
                register="neutral",
                unit_ref="a1-unit-2",
            ),
        ],
    ),
    PhrasebookCategory(
        id="time_a1",
        level="A1",
        situation="시간과 약속",
        icon="🕒",
        phrases=[
            PhrasebookEntry(
                text="지금 몇 시예요?",
                context="시간을 물을 때",
                register="neutral",
                unit_ref="a1-unit-3",
            ),
            PhrasebookEntry(
                text="오후 세 시에 만나요.",
                context="약속 시간을 정할 때",
                register="neutral",
                unit_ref="a1-unit-3",
            ),
            PhrasebookEntry(
                text="오늘은 월요일이에요.",
                context="요일을 말할 때",
                register="neutral",
                unit_ref="a1-unit-3",
            ),
        ],
    ),
    PhrasebookCategory(
        id="shopping_a1",
        level="A1",
        situation="기본 쇼핑",
        icon="🛒",
        phrases=[
            PhrasebookEntry(
                text="이거 얼마예요?",
                context="가격을 물을 때",
                register="neutral",
                unit_ref="a1-unit-7",
            ),
            PhrasebookEntry(
                text="이거 주세요.",
                context="물건을 살 때",
                register="neutral",
                unit_ref="a1-unit-7",
            ),
            PhrasebookEntry(
                text="카드로 계산할게요.",
                context="결제 방법을 말할 때",
                register="neutral",
                unit_ref="a1-unit-7",
            ),
        ],
    ),
]


def _extra_phrase(text: str, context: str, unit_ref: str) -> PhrasebookEntry:
    return PhrasebookEntry(text=text, context=context, register="neutral", unit_ref=unit_ref)


A1_CATEGORIES.append(
    PhrasebookCategory(
        id="expanded_daily_a1",
        level="A1",
        situation="기초 생활 표현",
        icon="🏠",
        phrases=[
            _extra_phrase(text, "기초 생활 상황에서 쓰는 표현", "a1-unit-8")
            for text in [
                "화장실은 어디예요?",
                "물이 필요해요.",
                "천천히 말해 주세요.",
                "다시 한번 말해 주세요.",
                "한국어로 뭐예요?",
                "잘 들리지 않아요.",
                "여기에 앉아도 돼요?",
                "창문을 열어도 돼요?",
                "오늘 날씨가 좋아요.",
                "조금 추워요.",
                "조금 더워요.",
                "이 길이 맞아요?",
                "역까지 가까워요?",
                "버스 정류장은 어디예요?",
                "이 버스가 시내에 가요?",
                "표 한 장 주세요.",
                "여기서 내려요?",
                "사진을 찍어도 돼요?",
                "이름을 써 주세요.",
                "전화번호를 알려 주세요.",
                "제 전화번호예요.",
                "가방을 잃어버렸어요.",
                "도와주세요.",
                "괜찮아요.",
                "미안해요.",
                "고마워요.",
                "정말 감사합니다.",
                "잠깐만요.",
                "지금 바빠요.",
                "나중에 만나요.",
                "내일 시간이 있어요?",
                "같이 갈까요?",
                "저는 배고파요.",
                "저는 목말라요.",
                "메뉴를 주세요.",
                "이거 맛있어요.",
                "맵지 않게 해 주세요.",
                "계산해 주세요.",
                "봉투 주세요.",
                "현금으로 낼게요.",
                "카드로 낼게요.",
                "영수증 주세요.",
                "이 색이 좋아요.",
                "다른 것도 보여 주세요.",
                "오늘 처음 왔어요.",
                "또 올게요.",
            ]
        ],
    )
)
