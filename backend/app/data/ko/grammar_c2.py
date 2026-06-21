"""C2 grammar topics — Korean (ko-KR)."""

from app.data._types import GrammarExample, GrammarMistake, GrammarTopic

C2_GRAMMAR_TOPICS: list[GrammarTopic] = [
    GrammarTopic(
        slug="semantic-precision",
        title="의미 정밀성",
        level="C2",
        category="정밀 표현",
        summary="의미 정밀성을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="의미 정밀성은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="의미 차이 + 맥락 선택",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="가능성이 있다와 가능성이 높다는 강도가 다릅니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="particle-nuance",
        title="조사 뉘앙스",
        level="C2",
        category="조사",
        summary="조사 뉘앙스을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="조사 뉘앙스은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="은/는, 이/가, 을/를의 미세한 차이",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="저는은 대비를 만들고 제가는 초점을 만듭니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="lexical-choice-register",
        title="어휘와 문체 선택",
        level="C2",
        category="문체",
        summary="어휘와 문체 선택을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="어휘와 문체 선택은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어휘 + 격식 + 분야",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="공식 문서에서는 줄이다보다 절감하다가 더 적절할 수 있습니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="expert-mediation",
        title="전문 내용 중재",
        level="C2",
        category="중재",
        summary="전문 내용 중재을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="전문 내용 중재은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="전문 개념 + 쉬운 설명",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="복잡한 절차를 단계별로 풀어 설명합니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="reformulation",
        title="재표현",
        level="C2",
        category="중재",
        summary="재표현을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="재표현은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="원문 의미 + 새로운 표현",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="전문 용어를 일상적인 말로 바꾸어 설명합니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="audience-adaptation",
        title="청중 맞춤 설명",
        level="C2",
        category="담화 전략",
        summary="청중 맞춤 설명을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="청중 맞춤 설명은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="청중 지식 + 설명 깊이",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="전문가에게는 근거를, 초보자에게는 예시를 먼저 제시합니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="critical-evaluation",
        title="비판적 평가",
        level="C2",
        category="비평",
        summary="비판적 평가을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="비판적 평가은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="근거 + 전제 + 반증",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="결론이 타당한지 자료와 전제를 함께 검토합니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="assumption-analysis",
        title="전제 분석",
        level="C2",
        category="비평",
        summary="전제 분석을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="전제 분석은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="숨은 전제 + 영향",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="이 주장은 모든 사용자가 같은 조건이라는 전제를 깔고 있습니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="rebuttal-structure",
        title="반박 구조",
        level="C2",
        category="비평",
        summary="반박 구조을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="반박 구조은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="상대 주장 + 반증 + 대안",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="그 주장에는 근거가 있지만 반대 사례도 존재합니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="translation-equivalence",
        title="번역 등가성",
        level="C2",
        category="번역",
        summary="번역 등가성을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="번역 등가성은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="의미 + 문체 + 기능",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="직역보다 기능이 같은 표현을 선택합니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="pragmatic-meaning",
        title="화용적 의미",
        level="C2",
        category="화용",
        summary="화용적 의미을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="화용적 의미은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="말의 의도 + 관계 + 상황",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="괜찮습니다가 실제로는 거절일 수 있습니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="cultural-transfer",
        title="문화적 전환",
        level="C2",
        category="번역",
        summary="문화적 전환을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="문화적 전환은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="문화 차이 + 설명 전략",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="직접 대응이 없을 때는 배경을 함께 설명합니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="rhetorical-strategy",
        title="수사 전략",
        level="C2",
        category="수사",
        summary="수사 전략을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="수사 전략은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="강조 + 대조 + 배열",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="문제의 심각성을 먼저 제시해 독자의 관심을 끕니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="emphasis-control",
        title="강조 조절",
        level="C2",
        category="수사",
        summary="강조 조절을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="강조 조절은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="강조 표현 + 균형",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="너무 강한 표현은 신뢰를 떨어뜨릴 수 있습니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="reader-positioning",
        title="독자 위치 설정",
        level="C2",
        category="수사",
        summary="독자 위치 설정을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="독자 위치 설정은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="독자 역할 + 관점 유도",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="독자를 문제 해결의 참여자로 위치시킵니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="language-history",
        title="한국어사의 맥락",
        level="C2",
        category="언어사",
        summary="한국어사의 맥락을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="한국어사의 맥락은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="역사 + 사회 + 표현 변화",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="한자어와 고유어의 쓰임은 시대와 분야에 따라 달라졌습니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="loanword-register",
        title="외래어와 문체",
        level="C2",
        category="어휘",
        summary="외래어와 문체을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="외래어와 문체은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="외래어 + 한자어 + 고유어 비교",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="미팅과 회의는 비슷하지만 문체와 분야가 다릅니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="diachronic-change",
        title="통시적 변화",
        level="C2",
        category="언어 변화",
        summary="통시적 변화을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="통시적 변화은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="시간에 따른 의미와 형태 변화",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="일부 표현은 세대에 따라 자연스러움이 다르게 느껴집니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="advanced-editing",
        title="고급 편집",
        level="C2",
        category="편집",
        summary="고급 편집을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="고급 편집은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="문장 수정 + 구조 조정",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="중복을 줄이고 핵심 주장을 앞으로 옮깁니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="cohesion-coherence",
        title="응집성과 일관성",
        level="C2",
        category="편집",
        summary="응집성과 일관성을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="응집성과 일관성은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="연결 표현 + 정보 흐름",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="앞 문장의 정보가 다음 문장의 출발점이 됩니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="style-revision",
        title="문체 재작성",
        level="C2",
        category="편집",
        summary="문체 재작성을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="문체 재작성은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="목적 + 독자 + 문체",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="친근한 글을 공식 안내문에 맞게 바꿉니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태는 맞지만 글의 흐름, 격식, 담화 기능과 맞지 않게 쓰는 경우",
                correct="문법 기능, 연결 관계, 높임 정도, 글의 목적을 함께 맞춰 자연스럽게 쓴다.",
                note="중급 이상에서는 형태 정확성뿐 아니라 담화 흐름과 레지스터를 함께 확인합니다.",
            )
        ],
        related=[],
    ),
]
