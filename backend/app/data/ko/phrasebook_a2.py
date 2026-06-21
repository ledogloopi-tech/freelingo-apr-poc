"""A2 phrasebook categories — Korean (ko-KR)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry

A2_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="travel_a2",
        level="A2",
        situation="여행과 숙박",
        icon="🧳",
        phrases=[
            PhrasebookEntry(
                text="예약했어요.",
                context="호텔이나 식당에서 예약을 알릴 때",
                register="neutral",
                unit_ref="a2-unit-1",
            ),
            PhrasebookEntry(
                text="방이 조용했으면 좋겠어요.",
                context="숙소 조건을 말할 때",
                register="neutral",
                unit_ref="a2-unit-1",
            ),
            PhrasebookEntry(
                text="체크인은 몇 시부터예요?",
                context="숙소 이용 시간을 물을 때",
                register="neutral",
                unit_ref="a2-unit-1",
            ),
        ],
    ),
    PhrasebookCategory(
        id="plans_a2",
        level="A2",
        situation="계획과 일정",
        icon="📅",
        phrases=[
            PhrasebookEntry(
                text="주말에 친구를 만날 거예요.",
                context="미래 계획을 말할 때",
                register="neutral",
                unit_ref="a2-unit-2",
            ),
            PhrasebookEntry(
                text="내일 전화할게요.",
                context="약속이나 결정을 말할 때",
                register="neutral",
                unit_ref="a2-unit-2",
            ),
            PhrasebookEntry(
                text="다음 주로 바꿀 수 있어요?",
                context="일정을 조정할 때",
                register="formal",
                unit_ref="a2-unit-2",
            ),
        ],
    ),
    PhrasebookCategory(
        id="health_a2",
        level="A2",
        situation="건강과 병원",
        icon="💊",
        phrases=[
            PhrasebookEntry(
                text="머리가 아파요.",
                context="증상을 말할 때",
                register="neutral",
                unit_ref="a2-unit-3",
            ),
            PhrasebookEntry(
                text="약을 먹어야 해요.",
                context="필요한 조치를 말할 때",
                register="neutral",
                unit_ref="a2-unit-3",
            ),
            PhrasebookEntry(
                text="병원에 가는 게 좋겠어요.",
                context="조언할 때",
                register="neutral",
                unit_ref="a2-unit-3",
            ),
        ],
    ),
    PhrasebookCategory(
        id="rules_a2",
        level="A2",
        situation="허락과 금지",
        icon="🚭",
        phrases=[
            PhrasebookEntry(
                text="여기 앉아도 돼요?",
                context="허락을 구할 때",
                register="neutral",
                unit_ref="a2-unit-4",
            ),
            PhrasebookEntry(
                text="사진을 찍으면 안 돼요.",
                context="금지 사항을 말할 때",
                register="neutral",
                unit_ref="a2-unit-4",
            ),
            PhrasebookEntry(
                text="신분증을 보여 주세요.",
                context="규칙에 따른 요청을 할 때",
                register="formal",
                unit_ref="a2-unit-4",
            ),
        ],
    ),
    PhrasebookCategory(
        id="transport_a2",
        level="A2",
        situation="교통과 길 찾기",
        icon="🚇",
        phrases=[
            PhrasebookEntry(
                text="오른쪽으로 가세요.",
                context="방향을 안내할 때",
                register="formal",
                unit_ref="a2-unit-7",
            ),
            PhrasebookEntry(
                text="지하철역이 어디예요?",
                context="장소를 물을 때",
                register="neutral",
                unit_ref="a2-unit-7",
            ),
            PhrasebookEntry(
                text="여기에서 내려야 해요.",
                context="하차 지점을 말할 때",
                register="neutral",
                unit_ref="a2-unit-7",
            ),
        ],
    ),
]
