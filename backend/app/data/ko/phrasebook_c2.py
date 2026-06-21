"""C2 phrasebook categories — Korean (ko-KR)."""

from app.data._types import PhrasebookCategory, PhrasebookEntry

C2_CATEGORIES: list[PhrasebookCategory] = [
    PhrasebookCategory(
        id="precision_c2",
        level="C2",
        situation="정밀한 표현",
        icon="🎯",
        phrases=[
            PhrasebookEntry(
                text="이 표현은 의미가 조금 달라집니다.",
                context="미세한 의미 차이를 설명할 때",
                register="formal",
                unit_ref="c2-unit-1",
            ),
            PhrasebookEntry(
                text="문맥상 더 중립적인 표현이 필요합니다.",
                context="어휘 선택을 조정할 때",
                register="formal",
                unit_ref="c2-unit-1",
            ),
            PhrasebookEntry(
                text="강한 단정은 피하는 편이 좋습니다.",
                context="표현 강도를 조절할 때",
                register="formal",
                unit_ref="c2-unit-1",
            ),
        ],
    ),
    PhrasebookCategory(
        id="mediation_c2",
        level="C2",
        situation="전문 내용 중재",
        icon="🔎",
        phrases=[
            PhrasebookEntry(
                text="전문 용어를 쉬운 말로 풀어 설명하겠습니다.",
                context="전문 내용을 설명할 때",
                register="formal",
                unit_ref="c2-unit-2",
            ),
            PhrasebookEntry(
                text="핵심은 절차가 세 단계라는 점입니다.",
                context="복잡한 정보를 단순화할 때",
                register="formal",
                unit_ref="c2-unit-2",
            ),
            PhrasebookEntry(
                text="대상에 따라 설명 방식을 바꿔야 합니다.",
                context="청중 맞춤을 말할 때",
                register="formal",
                unit_ref="c2-unit-2",
            ),
        ],
    ),
    PhrasebookCategory(
        id="critique_c2",
        level="C2",
        situation="비판과 반박",
        icon="⚖️",
        phrases=[
            PhrasebookEntry(
                text="이 주장의 전제를 먼저 검토해야 합니다.",
                context="비판적 평가를 시작할 때",
                register="formal",
                unit_ref="c2-unit-3",
            ),
            PhrasebookEntry(
                text="반증 사례도 함께 고려해야 합니다.",
                context="균형 잡힌 반박을 할 때",
                register="formal",
                unit_ref="c2-unit-3",
            ),
            PhrasebookEntry(
                text="결론을 더 제한적으로 제시하는 것이 타당합니다.",
                context="정밀한 결론을 말할 때",
                register="formal",
                unit_ref="c2-unit-3",
            ),
        ],
    ),
    PhrasebookCategory(
        id="translation_c2",
        level="C2",
        situation="번역과 등가성",
        icon="🌐",
        phrases=[
            PhrasebookEntry(
                text="직역보다 기능적으로 가까운 표현이 좋습니다.",
                context="번역 전략을 설명할 때",
                register="formal",
                unit_ref="c2-unit-4",
            ),
            PhrasebookEntry(
                text="문체와 공손성도 함께 옮겨야 합니다.",
                context="번역 기준을 말할 때",
                register="formal",
                unit_ref="c2-unit-4",
            ),
            PhrasebookEntry(
                text="문화적 배경을 보충 설명할 필요가 있습니다.",
                context="문화 차이를 중재할 때",
                register="formal",
                unit_ref="c2-unit-4",
            ),
        ],
    ),
]
