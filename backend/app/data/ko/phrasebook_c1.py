"""C1 phrasebook categories — Korean (ko-KR)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry

C1_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="academic_c1",
        level="C1",
        situation="학술적 요약",
        icon="🎓",
        phrases=[
            PhrasebookEntry(
                text="핵심 논점은 두 가지로 요약됩니다.",
                context="학술 내용을 요약할 때",
                register="formal",
                unit_ref="c1-unit-3",
            ),
            PhrasebookEntry(
                text="이 연구는 방법론에 한계가 있습니다.",
                context="연구를 평가할 때",
                register="formal",
                unit_ref="c1-unit-3",
            ),
            PhrasebookEntry(
                text="출처를 명확히 제시해야 합니다.",
                context="자료 사용을 말할 때",
                register="formal",
                unit_ref="c1-unit-3",
            ),
        ],
    ),
    PhrasebookCategory(
        id="public_discourse_c1",
        level="C1",
        situation="공적 담화",
        icon="🏛️",
        phrases=[
            PhrasebookEntry(
                text="이 문제는 사회 구조와 관련이 있습니다.",
                context="공적 주제를 설명할 때",
                register="formal",
                unit_ref="c1-unit-4",
            ),
            PhrasebookEntry(
                text="한편 다른 해석도 가능합니다.",
                context="균형 있게 말할 때",
                register="formal",
                unit_ref="c1-unit-4",
            ),
            PhrasebookEntry(
                text="필자는 비판적인 태도를 보입니다.",
                context="입장을 분석할 때",
                register="formal",
                unit_ref="c1-unit-4",
            ),
        ],
    ),
    PhrasebookCategory(
        id="style_c1",
        level="C1",
        situation="문체와 장르",
        icon="✍️",
        phrases=[
            PhrasebookEntry(
                text="이 표현은 너무 구어적입니다.",
                context="문체를 평가할 때",
                register="formal",
                unit_ref="c1-unit-5",
            ),
            PhrasebookEntry(
                text="공식 문서에는 더 적절한 표현이 필요합니다.",
                context="수정 방향을 말할 때",
                register="formal",
                unit_ref="c1-unit-5",
            ),
            PhrasebookEntry(
                text="장르에 맞게 구성을 바꿔야 합니다.",
                context="글쓰기 조언을 할 때",
                register="formal",
                unit_ref="c1-unit-5",
            ),
        ],
    ),
    PhrasebookCategory(
        id="negotiation_c1",
        level="C1",
        situation="협상과 설득",
        icon="🤝",
        phrases=[
            PhrasebookEntry(
                text="그 점은 이해하지만 다른 대안도 있습니다.",
                context="반론을 완곡하게 말할 때",
                register="formal",
                unit_ref="c1-unit-6",
            ),
            PhrasebookEntry(
                text="가능하시다면 일정을 조정하고 싶습니다.",
                context="협상에서 요청할 때",
                register="formal",
                unit_ref="c1-unit-6",
            ),
            PhrasebookEntry(
                text="서로 받아들일 수 있는 조건을 찾아봅시다.",
                context="합의를 제안할 때",
                register="formal",
                unit_ref="c1-unit-6",
            ),
        ],
    ),
]
