"""C1 grammar topics — Korean (ko-KR)."""

from app.data._types import GrammarExample, GrammarMistake, GrammarTopic

C1_GRAMMAR_TOPICS: list[GrammarTopic] = [
    GrammarTopic(
        slug="argument-structure",
        title="논증 구조",
        level="C1",
        category="논리",
        summary="논증 구조을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="논증 구조은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="배경 + 근거 + 반론 + 결론",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="먼저 배경을 제시하고 마지막에 결론을 정리합니다.",
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
        slug="concession-despite",
        title="양보 표현",
        level="C1",
        category="논리",
        summary="양보 표현을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="양보 표현은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="인정 + 그러나 + 주장",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="장점은 인정하지만 장기적 검토가 필요합니다.",
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
        slug="implication-hamui",
        title="함의 파악",
        level="C1",
        category="해석",
        summary="함의 파악을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="함의 파악은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="표현 + 맥락 + 숨은 의미",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="직접 말하지 않아도 우려가 드러납니다.",
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
        slug="advanced-honorifics",
        title="고급 높임말",
        level="C1",
        category="높임",
        summary="고급 높임말을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="고급 높임말은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="상대 + 상황 + 목적에 맞는 높임",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="자료를 검토해 주시면 감사하겠습니다.",
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
        slug="speech-level-shifts",
        title="말투 전환",
        level="C1",
        category="담화",
        summary="말투 전환을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="말투 전환은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="격식체와 해요체의 조절",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="발표에서는 격식체를 쓰고 질의응답에서는 부드럽게 말합니다.",
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
        slug="deference-strategies",
        title="공손 전략",
        level="C1",
        category="화용",
        summary="공손 전략을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="공손 전략은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="완곡함 + 이유 + 대안",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="가능하시다면 다음 주로 조정 부탁드립니다.",
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
        slug="academic-connectors",
        title="학술 연결 표현",
        level="C1",
        category="학술 문체",
        summary="학술 연결 표현을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="학술 연결 표현은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="한편/따라서/반면에",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="한편, 이 결과는 다른 해석도 가능하게 합니다.",
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
        slug="source-integration",
        title="출처 통합",
        level="C1",
        category="학술 문체",
        summary="출처 통합을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="출처 통합은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="출처 + 주장 + 해석",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="연구 결과에 따르면 이러한 경향이 확인됩니다.",
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
        slug="summary-compression",
        title="압축 요약",
        level="C1",
        category="요약",
        summary="압축 요약을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="압축 요약은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="핵심 주장 + 주요 근거",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="필자는 제도의 필요성과 위험을 함께 지적합니다.",
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
        slug="public-discourse-framing",
        title="공적 담화 구성",
        level="C1",
        category="담화 분석",
        summary="공적 담화 구성을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="공적 담화 구성은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="쟁점 + 이해관계 + 평가",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="이 문제는 개인 선택보다 사회 구조와 관련됩니다.",
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
        slug="stance-markers",
        title="입장 표지",
        level="C1",
        category="태도",
        summary="입장 표지을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="입장 표지은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="평가 표현 + 주장",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="필자는 다소 비판적인 태도를 보입니다.",
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
        slug="nuance-evaluation",
        title="뉘앙스 평가",
        level="C1",
        category="해석",
        summary="뉘앙스 평가을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="뉘앙스 평가은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어휘 선택 + 말투 + 맥락",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="그 표현은 중립적이라기보다 조심스러운 느낌을 줍니다.",
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
        slug="register-control",
        title="문체 조절",
        level="C1",
        category="문체",
        summary="문체 조절을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="문체 조절은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="상황 + 독자 + 목적",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="보고서에서는 구어체보다 격식 있는 표현을 씁니다.",
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
        slug="genre-conventions",
        title="장르 관습",
        level="C1",
        category="장르",
        summary="장르 관습을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="장르 관습은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="장르별 구성과 표현",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="논설문은 주장과 근거가 분명해야 합니다.",
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
        slug="nominal-style-formal",
        title="명사 중심 공식 문체",
        level="C1",
        category="문체",
        summary="명사 중심 공식 문체을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="명사 중심 공식 문체은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동작 명사 + 필요/가능/검토",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="제도의 개선이 필요합니다.",
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
        slug="hedging-requests",
        title="완곡한 요청",
        level="C1",
        category="협상",
        summary="완곡한 요청을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="완곡한 요청은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="부담 완화 + 요청",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="번거로우시겠지만 확인 부탁드립니다.",
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
        slug="negotiation-framing",
        title="협상 틀 잡기",
        level="C1",
        category="협상",
        summary="협상 틀 잡기을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="협상 틀 잡기은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="목표 + 조건 + 대안",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="일정을 조정하되 마감은 유지하고 싶습니다.",
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
        slug="counterproposal",
        title="대안 제시",
        level="C1",
        category="협상",
        summary="대안 제시을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="대안 제시은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="인정 + 다른 제안",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="그 방법도 좋지만 다른 방안을 검토해 보면 어떨까요?",
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
        slug="figurative-language",
        title="비유 표현",
        level="C1",
        category="문학",
        summary="비유 표현을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="비유 표현은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="비유 + 맥락 + 효과",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="그 말은 마음에 오래 남는 그림자 같았습니다.",
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
        slug="implicit-subjects-korean",
        title="생략된 주어",
        level="C1",
        category="해석",
        summary="생략된 주어을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="생략된 주어은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="문맥에서 주어 보완",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="문맥상 행동한 사람은 앞 문장의 화자입니다.",
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
        slug="cultural-allusion",
        title="문화적 암시",
        level="C1",
        category="문화",
        summary="문화적 암시을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="문화적 암시은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="배경 지식 + 표현",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="전통 명절의 이미지를 빌려 공동체성을 강조합니다.",
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
