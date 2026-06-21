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


def _extra_phrase(text: str, context: str, unit_ref: str) -> PhrasebookEntry:
    return PhrasebookEntry(text=text, context=context, register="formal", unit_ref=unit_ref)


C2_CATEGORIES.append(
    PhrasebookCategory(
        id="expanded_synthesis_c2",
        level="C2",
        situation="전문적 통합과 비판",
        icon="🧩",
        phrases=[
            _extra_phrase(text, "전문적 통합, 번역, 비판적 평가에서 쓰는 표현", "c2-unit-8")
            for text in [
                "여러 관점을 통합하면 다른 결론이 도출됩니다.",
                "이 논의는 용어 정의부터 재검토해야 합니다.",
                "전문성을 유지하면서도 표현을 쉽게 바꾸겠습니다.",
                "원문의 함의를 해치지 않는 범위에서 재구성했습니다.",
                "직역하면 자연스럽지 않으므로 기능적으로 옮겼습니다.",
                "문체와 공손성도 함께 반영해야 합니다.",
                "문화적 배경을 보충하면 의미가 더 분명해집니다.",
                "핵심만 추려 말하면 다음과 같습니다.",
                "이 주장의 전제는 아직 충분히 검토되지 않았습니다.",
                "반증 사례를 포함하면 결론이 더 제한됩니다.",
                "논리는 명확하지만 근거 제시가 약합니다.",
                "가치 판단을 명시해야 논의가 정리됩니다.",
                "공공성의 관점에서 다시 판단해야 합니다.",
                "투명성이 확보되지 않으면 신뢰를 얻기 어렵습니다.",
                "공정성과 효율성 사이에 긴장이 있습니다.",
                "당사자의 목소리를 논의에 포함해야 합니다.",
                "이 판단을 정당화할 근거가 필요합니다.",
                "단기 성과와 장기 책임을 나누어 보겠습니다.",
                "합의 형성에는 충분한 설명이 필요합니다.",
                "전문 용어를 피해서 다시 설명하겠습니다.",
                "엄밀히 말하면 두 조건을 구분해야 합니다.",
                "예외적인 경우가 있지만 원칙은 같습니다.",
                "상관관계와 인과관계를 혼동하면 안 됩니다.",
                "이 자료만으로는 단정하기 어렵습니다.",
                "배경 지식을 보충하면 이해하기 쉬워집니다.",
                "결론을 한 문장으로 요약하겠습니다.",
                "반대 의견을 포함하면 주장이 더 강해집니다.",
                "논점을 다시 배열하면 설득력이 높아집니다.",
                "표현의 강도를 낮추면 더 균형 있게 들립니다.",
                "이 해석은 가능한 여러 해석 중 하나입니다.",
                "원문과 번역문의 효과가 완전히 같지는 않습니다.",
                "청중에 따라 설명 방식을 조정해야 합니다.",
                "최종 결론은 조건부로 제시하는 것이 타당합니다.",
                "논의를 더 정밀하게 재구성하겠습니다.",
            ]
        ],
    )
)
