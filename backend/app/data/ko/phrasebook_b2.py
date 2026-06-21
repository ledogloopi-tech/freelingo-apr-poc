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


def _extra_phrase(text: str, context: str, unit_ref: str) -> PhrasebookEntry:
    return PhrasebookEntry(text=text, context=context, register="formal", unit_ref=unit_ref)


B2_CATEGORIES.append(
    PhrasebookCategory(
        id="expanded_professional_b2",
        level="B2",
        situation="업무 분석과 논의",
        icon="📊",
        phrases=[
            _extra_phrase(text, "업무, 분석, 토론 상황에서 쓰는 표현", "b2-unit-8")
            for text in [
                "현재 상황을 기준으로 판단해야 합니다.",
                "이 자료는 중요한 근거가 됩니다.",
                "통계를 해석할 때 주의가 필요합니다.",
                "다른 관점에서도 검토해 보겠습니다.",
                "이 주장에는 설득력이 있습니다.",
                "다만 전제가 조금 약합니다.",
                "구체적인 사례를 추가하면 좋겠습니다.",
                "비용 대비 효과를 확인해야 합니다.",
                "고객에게 미치는 영향이 큽니다.",
                "운영 부담도 함께 고려해야 합니다.",
                "우선순위를 다시 정리하겠습니다.",
                "관련 부서와 조율하겠습니다.",
                "일정 조정이 필요해 보입니다.",
                "위험 요소를 미리 공유해야 합니다.",
                "대안을 세 가지로 정리했습니다.",
                "이 선택지는 현실적입니다.",
                "하지만 장기적인 효과는 불확실합니다.",
                "계약 조건을 다시 확인하겠습니다.",
                "예산 범위 안에서 진행해야 합니다.",
                "결정 전에 추가 검토가 필요합니다.",
                "회의록에 합의 내용을 남기겠습니다.",
                "다음 단계는 자료 검토입니다.",
                "이 문장은 조금 강하게 들립니다.",
                "더 중립적인 표현으로 바꾸겠습니다.",
                "핵심 메시지를 앞에 두는 것이 좋습니다.",
                "결론을 더 명확하게 써야 합니다.",
                "독자의 반응도 고려해야 합니다.",
                "이 보도는 배경 설명이 부족합니다.",
                "전문가 의견을 추가로 확인하겠습니다.",
                "근거와 의견을 구분해야 합니다.",
                "이 문제는 경제와도 연결됩니다.",
                "단기 효과와 장기 효과를 나누어 보겠습니다.",
                "이 부분은 반론이 예상됩니다.",
                "반론에 대한 답변도 준비하겠습니다.",
                "최종 판단은 다음 회의에서 하겠습니다.",
                "오늘 논의한 내용을 정리해 공유하겠습니다.",
                "추가 자료가 있으면 보내 주세요.",
            ]
        ],
    )
)
