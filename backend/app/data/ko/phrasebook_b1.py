"""B1 phrasebook categories — Korean (ko-KR)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry

B1_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="opinions_b1",
        level="B1",
        situation="의견 말하기",
        icon="💬",
        phrases=[
            PhrasebookEntry(
                text="저는 이 방법이 좋다고 생각해요.",
                context="의견을 말할 때",
                register="neutral",
                unit_ref="b1-unit-1",
            ),
            PhrasebookEntry(
                text="그 이유는 시간이 절약되기 때문이에요.",
                context="근거를 설명할 때",
                register="neutral",
                unit_ref="b1-unit-1",
            ),
            PhrasebookEntry(
                text="다른 의견도 이해해요.",
                context="상대 의견을 인정할 때",
                register="neutral",
                unit_ref="b1-unit-1",
            ),
        ],
    ),
    PhrasebookCategory(
        id="stories_b1",
        level="B1",
        situation="경험 이야기",
        icon="📖",
        phrases=[
            PhrasebookEntry(
                text="처음에는 어려웠는데 점점 익숙해졌어요.",
                context="경험의 변화를 말할 때",
                register="neutral",
                unit_ref="b1-unit-2",
            ),
            PhrasebookEntry(
                text="밥을 먹고 나서 산책했어요.",
                context="사건 순서를 설명할 때",
                register="neutral",
                unit_ref="b1-unit-2",
            ),
            PhrasebookEntry(
                text="음악을 들으면서 공부했어요.",
                context="동시 행동을 말할 때",
                register="neutral",
                unit_ref="b1-unit-2",
            ),
        ],
    ),
    PhrasebookCategory(
        id="advice_b1",
        level="B1",
        situation="조언과 제안",
        icon="🧭",
        phrases=[
            PhrasebookEntry(
                text="조금 쉬는 게 어때요?",
                context="부드럽게 제안할 때",
                register="neutral",
                unit_ref="b1-unit-3",
            ),
            PhrasebookEntry(
                text="일찍 출발하는 게 좋아요.",
                context="권장할 때",
                register="neutral",
                unit_ref="b1-unit-3",
            ),
            PhrasebookEntry(
                text="무리하지 않는 게 좋겠어요.",
                context="상대 건강을 배려할 때",
                register="neutral",
                unit_ref="b1-unit-3",
            ),
        ],
    ),
    PhrasebookCategory(
        id="requests_b1",
        level="B1",
        situation="공손한 요청과 거절",
        icon="🙇",
        phrases=[
            PhrasebookEntry(
                text="문을 닫아 주실 수 있어요?",
                context="정중하게 부탁할 때",
                register="formal",
                unit_ref="b1-unit-5",
            ),
            PhrasebookEntry(
                text="죄송하지만 오늘은 어렵겠어요.",
                context="부드럽게 거절할 때",
                register="formal",
                unit_ref="b1-unit-5",
            ),
            PhrasebookEntry(
                text="도와주셔서 감사합니다.",
                context="도움을 받은 뒤 감사할 때",
                register="formal",
                unit_ref="b1-unit-5",
            ),
        ],
    ),
    PhrasebookCategory(
        id="problems_b1",
        level="B1",
        situation="문제 해결",
        icon="🛠️",
        phrases=[
            PhrasebookEntry(
                text="문제가 생겼어요.",
                context="문제를 알릴 때",
                register="neutral",
                unit_ref="b1-unit-7",
            ),
            PhrasebookEntry(
                text="다시 확인해 주시겠어요?",
                context="해결을 요청할 때",
                register="formal",
                unit_ref="b1-unit-7",
            ),
            PhrasebookEntry(
                text="다음에는 이렇게 해 보겠습니다.",
                context="해결 방안을 말할 때",
                register="formal",
                unit_ref="b1-unit-7",
            ),
        ],
    ),
]
