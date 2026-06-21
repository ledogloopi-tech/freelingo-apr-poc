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


def _extra_phrase(text: str, context: str, unit_ref: str) -> PhrasebookEntry:
    return PhrasebookEntry(text=text, context=context, register="neutral", unit_ref=unit_ref)


A2_CATEGORIES.append(
    PhrasebookCategory(
        id="expanded_services_a2",
        level="A2",
        situation="예약과 서비스",
        icon="🧾",
        phrases=[
            _extra_phrase(text, "예약, 이동, 서비스 상황에서 쓰는 표현", "a2-unit-8")
            for text in [
                "예약을 확인하고 싶어요.",
                "예약 시간을 바꿀 수 있을까요?",
                "내일 오후는 가능해요?",
                "취소하려면 어떻게 해야 해요?",
                "확인 문자를 보내 주세요.",
                "조금 늦을 것 같아요.",
                "길이 막혀서 늦었어요.",
                "다음 기차는 몇 시예요?",
                "어디에서 갈아타야 해요?",
                "왕복 표를 사고 싶어요.",
                "짐을 맡길 수 있어요?",
                "방을 바꿀 수 있을까요?",
                "에어컨이 잘 안 돼요.",
                "수건을 더 주세요.",
                "조식은 몇 시부터예요?",
                "체크아웃 시간을 알고 싶어요.",
                "이 옷을 입어 봐도 돼요?",
                "다른 사이즈가 있어요?",
                "환불하고 싶어요.",
                "교환할 수 있을까요?",
                "영수증이 필요해요.",
                "증상이 언제부터 있었어요?",
                "열이 조금 있어요.",
                "약은 언제 먹어야 해요?",
                "하루에 몇 번 먹어요?",
                "보험증을 가져왔어요.",
                "오늘은 쉬는 게 좋겠어요.",
                "운동을 시작하려고 해요.",
                "주말에 등산할 거예요.",
                "친구를 초대했어요.",
                "모임 장소를 알려 주세요.",
                "참가비는 얼마예요?",
                "먼저 연락드릴게요.",
                "확인하고 다시 말씀드릴게요.",
                "이 부분을 설명해 주세요.",
                "좀 더 쉽게 말해 주세요.",
                "한국어로 설명해 볼게요.",
                "제가 이해한 게 맞아요?",
                "그 방법이 더 편해요.",
                "다른 방법도 있어요?",
                "시간이 맞으면 갈게요.",
                "오늘은 참석하기 어려워요.",
                "다음에 같이 가요.",
            ]
        ],
    )
)
