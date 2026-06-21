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


def _extra_phrase(text: str, context: str, unit_ref: str) -> PhrasebookEntry:
    return PhrasebookEntry(text=text, context=context, register="formal", unit_ref=unit_ref)


C1_CATEGORIES.append(
    PhrasebookCategory(
        id="expanded_nuance_c1",
        level="C1",
        situation="정교한 표현과 의사결정",
        icon="🎚️",
        phrases=[
            _extra_phrase(text, "정교한 설명, 협상, 발표에서 쓰는 표현", "c1-unit-8")
            for text in [
                "이 표현은 맥락에 따라 다르게 해석될 수 있습니다.",
                "조금 더 완곡하게 표현하는 편이 적절합니다.",
                "상대방의 우려를 충분히 이해하고 있습니다.",
                "다만 현실적인 제약도 고려해야 합니다.",
                "양측 모두 수용할 수 있는 대안을 찾고 싶습니다.",
                "조건을 명확히 한 뒤에 합의하는 것이 좋겠습니다.",
                "결론을 내리기 전에 전제를 확인하겠습니다.",
                "책임 범위를 문서로 남겨야 합니다.",
                "이 자료의 신뢰성을 먼저 검토해야 합니다.",
                "선행 연구에서는 이 부분을 충분히 다루지 않았습니다.",
                "조사 방법에는 몇 가지 한계가 있습니다.",
                "결과를 해석할 때 주의가 필요합니다.",
                "다른 설명 가능성도 열어 두어야 합니다.",
                "용어를 먼저 정의하고 논의를 시작하겠습니다.",
                "핵심은 원인과 결과를 구분하는 것입니다.",
                "논점을 세 가지로 나누어 설명하겠습니다.",
                "이 선택지는 타당하지만 위험 관리가 필요합니다.",
                "단기적인 이익만으로 판단하기는 어렵습니다.",
                "이 결정은 장기적인 책임과 연결됩니다.",
                "상대방의 의도를 고려해 답변하겠습니다.",
                "사실관계와 평가를 구분해서 말씀드리겠습니다.",
                "해당 표현은 다소 직접적으로 들릴 수 있습니다.",
                "공손성은 유지하면서 문장을 줄일 수 있습니다.",
                "요청의 부담을 줄이는 표현이 필요합니다.",
                "거절하더라도 감사의 뜻을 먼저 전하겠습니다.",
                "첨부 자료를 참고해 주시면 이해가 쉬울 것입니다.",
                "궁금한 점이 있으면 언제든지 알려 주세요.",
                "논의의 범위를 조금 좁히겠습니다.",
                "결론은 조건부로 제시하는 것이 안전합니다.",
                "후속 과제로 남겨 두는 것이 좋겠습니다.",
                "요약하면 실행 체계가 가장 큰 쟁점입니다.",
                "판단 자료가 충분해진 뒤 결정하겠습니다.",
                "오늘 논의는 여기서 마무리하겠습니다.",
            ]
        ],
    )
)
