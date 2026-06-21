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
            PhrasebookEntry(
                text="예약을 확인하고 싶어요.",
                context="예약 확인을 요청할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="예약 시간을 바꿀 수 있을까요?",
                context="예약 변경을 요청할 때",
                register="formal",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="내일 오후는 가능해요?",
                context="가능 시간을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="취소하려면 어떻게 해야 해요?",
                context="취소 방법을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="확인 문자를 보내 주세요.",
                context="확인 메시지를 요청할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="조금 늦을 것 같아요.",
                context="지각을 알릴 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="길이 막혀서 늦었어요.",
                context="지각 이유를 설명할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="다음 기차는 몇 시예요?",
                context="기차 시간을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="어디에서 갈아타야 해요?",
                context="환승 정보를 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="왕복 표를 사고 싶어요.",
                context="왕복 티켓을 구매할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="짐을 맡길 수 있어요?",
                context="수하물 보관을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="방을 바꿀 수 있을까요?",
                context="객실 변경을 요청할 때",
                register="formal",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="에어컨이 잘 안 돼요.",
                context="시설 문제를 알릴 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="수건을 더 주세요.",
                context="추가 용품을 요청할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="조식은 몇 시부터예요?",
                context="식사 시간을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="체크아웃 시간을 알고 싶어요.",
                context="퇴실 시간을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="이 옷을 입어 봐도 돼요?",
                context="의류를 시착할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="다른 사이즈가 있어요?",
                context="다른 치수를 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="환불하고 싶어요.",
                context="환불을 요청할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="교환할 수 있을까요?",
                context="교환을 요청할 때",
                register="formal",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="영수증이 필요해요.",
                context="영수증이 필요할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="증상이 언제부터 있었어요?",
                context="병원에서 증상 시기를 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="열이 조금 있어요.",
                context="증상을 설명할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="약은 언제 먹어야 해요?",
                context="복용 시간을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="하루에 몇 번 먹어요?",
                context="복용 횟수를 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="보험증을 가져왔어요.",
                context="보험 서류를 제시할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="오늘은 쉬는 게 좋겠어요.",
                context="휴식이 필요함을 말할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="운동을 시작하려고 해요.",
                context="새로운 계획을 말할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="주말에 등산할 거예요.",
                context="주말 계획을 말할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="친구를 초대했어요.",
                context="초대 사실을 말할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="모임 장소를 알려 주세요.",
                context="모임 장소를 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="참가비는 얼마예요?",
                context="참가 비용을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="먼저 연락드릴게요.",
                context="나중에 연락하겠다고 할 때",
                register="formal",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="확인하고 다시 말씀드릴게요.",
                context="추후 확인을 약속할 때",
                register="formal",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="이 부분을 설명해 주세요.",
                context="설명을 요청할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="좀 더 쉽게 말해 주세요.",
                context="쉬운 설명을 요청할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="한국어로 설명해 볼게요.",
                context="한국어로 시도하겠다고 할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="제가 이해한 게 맞아요?",
                context="이해를 확인할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="그 방법이 더 편해요.",
                context="선호하는 방법을 말할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="다른 방법도 있어요?",
                context="대안을 물을 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="시간이 맞으면 갈게요.",
                context="조건부 약속을 할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="오늘은 참석하기 어려워요.",
                context="불참을 알릴 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
            PhrasebookEntry(
                text="다음에 같이 가요.",
                context="다음 기회를 약속할 때",
                register="neutral",
                unit_ref="a2-unit-8",
            ),
        ],
    )
)
