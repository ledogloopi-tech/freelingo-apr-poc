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
            PhrasebookEntry(
                text="화장실은 어디예요?",
                context="장소를 물을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="물이 필요해요.",
                context="필요한 것을 말할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="천천히 말해 주세요.",
                context="말 속도를 조절해 달라고 할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="다시 한번 말해 주세요.",
                context="상대 말을 다시 듣고 싶을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="한국어로 뭐예요?",
                context="단어 뜻을 물을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="잘 들리지 않아요.",
                context="소리가 잘 안 들릴 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="여기에 앉아도 돼요?",
                context="자리 사용 허락을 구할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="창문을 열어도 돼요?",
                context="환기 허락을 구할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="오늘 날씨가 좋아요.",
                context="날씨 이야기를 꺼낼 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="조금 추워요.",
                context="추위를 느낄 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="조금 더워요.",
                context="더위를 느낄 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="이 길이 맞아요?",
                context="길을 확인할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="역까지 가까워요?",
                context="거리를 물을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="버스 정류장은 어디예요?",
                context="대중교통 정보를 물을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="이 버스가 시내에 가요?",
                context="노선을 확인할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="표 한 장 주세요.",
                context="티켓을 구매할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="여기서 내려요?",
                context="하차 여부를 물을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="사진을 찍어도 돼요?",
                context="사진 촬영 허락을 구할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="이름을 써 주세요.",
                context="개인 정보를 요청할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="전화번호를 알려 주세요.",
                context="연락처를 물을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="제 전화번호예요.",
                context="자신의 연락처를 알려줄 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="가방을 잃어버렸어요.",
                context="분실물을 신고할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="도와주세요.",
                context="긴급히 도움을 요청할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="괜찮아요.",
                context="상대를 안심시킬 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="미안해요.",
                context="가볍게 사과할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="고마워요.",
                context="가볍게 감사할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="정말 감사합니다.",
                context="진심으로 감사할 때",
                register="formal",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="잠깐만요.",
                context="잠시 기다려 달라고 할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="지금 바빠요.",
                context="상황을 설명할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="나중에 만나요.",
                context="헤어지며 약속할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="내일 시간이 있어요?",
                context="약속 가능 여부를 물을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="같이 갈까요?",
                context="함께 가자고 제안할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="저는 배고파요.",
                context="배고픔을 말할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="저는 목말라요.",
                context="목마름을 말할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="메뉴를 주세요.",
                context="식당에서 메뉴판을 요청할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="이거 맛있어요.",
                context="음식 맛을 평가할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="맵지 않게 해 주세요.",
                context="주문 시 요청할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="계산해 주세요.",
                context="식사 후 계산할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="봉투 주세요.",
                context="쇼핑백을 요청할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="현금으로 낼게요.",
                context="현금 결제를 말할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="카드로 낼게요.",
                context="카드 결제를 말할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="영수증 주세요.",
                context="영수증을 요청할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="이 색이 좋아요.",
                context="색상 선호를 말할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="다른 것도 보여 주세요.",
                context="다른 상품을 보고 싶을 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="오늘 처음 왔어요.",
                context="첫 방문임을 알릴 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
            PhrasebookEntry(
                text="또 올게요.",
                context="재방문 의사를 말할 때",
                register="neutral",
                unit_ref="a1-unit-8",
            ),
        ],
    )
)
