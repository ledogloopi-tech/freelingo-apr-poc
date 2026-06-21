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


def _extra_phrase(text: str, context: str, unit_ref: str) -> PhrasebookEntry:
    return PhrasebookEntry(text=text, context=context, register="neutral", unit_ref=unit_ref)


B1_CATEGORIES.append(
    PhrasebookCategory(
        id="expanded_discussion_b1",
        level="B1",
        situation="경험과 의견 설명",
        icon="💬",
        phrases=[
            PhrasebookEntry(
                text="제 생각에는 준비가 더 필요해요.",
                context="의견을 조심스럽게 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="그 이유는 두 가지예요.",
                context="이유 개수를 제시할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="예를 들면 이런 상황이 있어요.",
                context="구체적 예시를 들 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="저도 비슷한 경험이 있어요.",
                context="공감을 표현할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="처음에는 어려웠지만 익숙해졌어요.",
                context="변화된 경험을 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="이 경험을 통해 많이 배웠어요.",
                context="경험의 교훈을 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="그 의견에는 어느 정도 동의해요.",
                context="부분적 동의를 표현할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="하지만 다른 문제도 있다고 생각해요.",
                context="반대 의견을 제시할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="장점과 단점을 함께 봐야 해요.",
                context="균형 잡힌 판단을 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="단기적으로는 편리해요.",
                context="단기적 관점을 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="장기적으로는 걱정되는 점이 있어요.",
                context="장기적 우려를 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="지역 사람들의 의견을 들어야 해요.",
                context="의견 수렴 필요를 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="환경을 위해 작은 실천이 필요해요.",
                context="환경 보호를 주장할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="안전을 위해 규칙을 지켜야 해요.",
                context="안전 규칙을 강조할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="문제를 나누어서 생각해 봅시다.",
                context="문제 분석을 제안할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="먼저 원인을 확인해야 해요.",
                context="원인 파악이 필요할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="해결 방법을 같이 찾아봐요.",
                context="협력을 제안할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="이 방법은 현실적이라고 생각해요.",
                context="해결책을 평가할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="비용이 가장 큰 문제예요.",
                context="주요 장애를 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="시간이 충분하지 않을 수도 있어요.",
                context="제약을 언급할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="팀에서 역할을 나누면 좋아요.",
                context="역할 분담을 제안할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="자료를 먼저 확인해 주세요.",
                context="사전 검토를 요청할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="발표 내용을 정리해 봤어요.",
                context="정리 결과를 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="질문이 있으면 말씀해 주세요.",
                context="질문을 유도할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="이 부분은 다시 설명하겠습니다.",
                context="재설명을 약속할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="결론부터 말씀드리면 가능합니다.",
                context="결론을 먼저 제시할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="아직 결정하기는 어려워요.",
                context="판단 보류를 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="조금 더 생각해 보고 싶어요.",
                context="숙고 시간을 요청할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="상황에 따라 답이 달라질 수 있어요.",
                context="조건부 판단을 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="상대방 입장도 이해해야 해요.",
                context="공감 필요성을 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="오해가 있었던 것 같아요.",
                context="오해 가능성을 언급할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="제가 잘못 이해했을 수도 있어요.",
                context="자신의 오해를 인정할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="다시 확인해 보겠습니다.",
                context="재확인을 약속할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="도와주셔서 정말 감사합니다.",
                context="도움에 깊이 감사할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="다음에는 더 잘 준비하겠습니다.",
                context="개선 의지를 말할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="이 경험이 큰 도움이 됐어요.",
                context="경험의 가치를 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="앞으로도 계속 연습하고 싶어요.",
                context="지속 의지를 말할 때",
                register="neutral",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="마지막으로 핵심을 정리하겠습니다.",
                context="최종 요약을 할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="첫 번째는 시간 문제입니다.",
                context="첫째 논점을 제시할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="두 번째는 비용 문제입니다.",
                context="둘째 논점을 제시할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
            PhrasebookEntry(
                text="그래서 단계적으로 진행하는 것이 좋겠습니다.",
                context="최종 제안을 할 때",
                register="formal",
                unit_ref="b1-unit-8",
            ),
        ],
    )
)
