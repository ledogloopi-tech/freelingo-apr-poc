"""B2 phrasebook categories — Korean (ko-KR)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry

B2_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="debate_b2",
        level="B2",
        situation="토론과 근거",
        icon="🗣️",
        phrases=[
            PhrasebookEntry(
                text="자료에 따르면 이용자가 늘었습니다.",
                context="근거를 제시할 때",
                register="formal",
                unit_ref="b2-unit-1",
            ),
            PhrasebookEntry(
                text="효과가 있기는 하지만 비용도 고려해야 합니다.",
                context="양보 후 반론할 때",
                register="formal",
                unit_ref="b2-unit-1",
            ),
            PhrasebookEntry(
                text="저는 단계적 도입이 바람직하다고 봅니다.",
                context="입장을 정리할 때",
                register="formal",
                unit_ref="b2-unit-1",
            ),
        ],
    ),
    PhrasebookCategory(
        id="meetings_b2",
        level="B2",
        situation="회의와 업무",
        icon="🏢",
        phrases=[
            PhrasebookEntry(
                text="오늘 안건을 말씀드리겠습니다.",
                context="회의를 시작할 때",
                register="formal",
                unit_ref="b2-unit-2",
            ),
            PhrasebookEntry(
                text="자료를 보내 드리겠습니다.",
                context="업무상 약속할 때",
                register="formal",
                unit_ref="b2-unit-2",
            ),
            PhrasebookEntry(
                text="확인 후 다시 연락드리겠습니다.",
                context="후속 조치를 말할 때",
                register="formal",
                unit_ref="b2-unit-2",
            ),
        ],
    ),
    PhrasebookCategory(
        id="analysis_b2",
        level="B2",
        situation="분석과 추측",
        icon="📊",
        phrases=[
            PhrasebookEntry(
                text="이 결과는 의미가 있을 것 같습니다.",
                context="조심스럽게 판단할 때",
                register="formal",
                unit_ref="b2-unit-3",
            ),
            PhrasebookEntry(
                text="수요가 더 늘어날 것으로 보입니다.",
                context="추세를 말할 때",
                register="formal",
                unit_ref="b2-unit-3",
            ),
            PhrasebookEntry(
                text="몇 가지 원인을 생각해 볼 수 있습니다.",
                context="분석을 시작할 때",
                register="formal",
                unit_ref="b2-unit-3",
            ),
        ],
    ),
    PhrasebookCategory(
        id="relationships_b2",
        level="B2",
        situation="관계와 감정",
        icon="🤝",
        phrases=[
            PhrasebookEntry(
                text="그렇게 느낄 수밖에 없었어요.",
                context="불가피한 감정을 설명할 때",
                register="neutral",
                unit_ref="b2-unit-5",
            ),
            PhrasebookEntry(
                text="미리 말할 걸 그랬어요.",
                context="후회를 표현할 때",
                register="neutral",
                unit_ref="b2-unit-5",
            ),
            PhrasebookEntry(
                text="좋기는 한데 조금 걱정돼요.",
                context="완곡하게 반대할 때",
                register="neutral",
                unit_ref="b2-unit-5",
            ),
        ],
    ),
    PhrasebookCategory(
        id="media_b2",
        level="B2",
        situation="매체와 비판",
        icon="📰",
        phrases=[
            PhrasebookEntry(
                text="보도에 따르면 상황이 달라졌습니다.",
                context="뉴스 출처를 언급할 때",
                register="formal",
                unit_ref="b2-unit-7",
            ),
            PhrasebookEntry(
                text="필자의 입장은 신중해 보입니다.",
                context="글쓴이 태도를 말할 때",
                register="formal",
                unit_ref="b2-unit-7",
            ),
            PhrasebookEntry(
                text="사실과 의견을 구분해야 합니다.",
                context="비판적으로 읽을 때",
                register="formal",
                unit_ref="b2-unit-7",
            ),
        ],
    ),
]
