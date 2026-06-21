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
