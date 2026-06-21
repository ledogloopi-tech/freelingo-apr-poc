"""B1 grammar topics — Korean (ko-KR)."""

from app.data._types import GrammarExample, GrammarMistake, GrammarTopic

B1_GRAMMAR_TOPICS: list[GrammarTopic] = [
    GrammarTopic(
        slug="opinion-think-go-saenggakhaeyo",
        title="고 생각해요 의견",
        level="B1",
        category="의견",
        summary="고 생각해요 의견을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="고 생각해요 의견은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="문장 + 고 생각해요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="이 방법이 좋다고 생각해요.",
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
        slug="reason-gi-ttaemune",
        title="기 때문에 이유",
        level="B1",
        category="이유",
        summary="기 때문에 이유을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="기 때문에 이유은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사/형용사 어간 + 기 때문에",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="시간이 없기 때문에 먼저 갈게요.",
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
        slug="quote-dago-haeyo",
        title="다고 해요 전달",
        level="B1",
        category="인용",
        summary="다고 해요 전달을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="다고 해요 전달은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="문장 + 다고 해요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="내일 비가 온다고 해요.",
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
        slug="while-myeonseo",
        title="면서 동시 동작",
        level="B1",
        category="연결",
        summary="면서 동시 동작을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="면서 동시 동작은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 으면서/면서",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="음악을 들으면서 공부해요.",
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
        slug="sequence-go-naseo",
        title="고 나서 순서",
        level="B1",
        category="순서",
        summary="고 나서 순서을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="고 나서 순서은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 고 나서",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="밥을 먹고 나서 산책했어요.",
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
        slug="background-neunde",
        title="는데 배경",
        level="B1",
        category="배경",
        summary="는데 배경을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="는데 배경은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 는데/은데",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="길을 찾고 있는데 도와주실 수 있어요?",
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
        slug="advice-neun-ge-eottaeyo",
        title="는 게 어때요 조언",
        level="B1",
        category="조언",
        summary="는 게 어때요 조언을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="는 게 어때요 조언은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 는 게 어때요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="조금 쉬는 게 어때요?",
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
        slug="better-neun-ge-joayo",
        title="는 게 좋아요 권장",
        level="B1",
        category="조언",
        summary="는 게 좋아요 권장을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="는 게 좋아요 권장은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="일찍 출발하는 게 좋아요.",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="비가 오니까 우산을 가져가는 게 좋아요.",
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
        slug="should-aya-getseoyo",
        title="아야겠어요 결심",
        level="B1",
        category="필요",
        summary="아야겠어요 결심을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="아야겠어요 결심은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 아야/어야겠어요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="운동을 더 해야겠어요.",
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
        slug="conditional-eumyeon",
        title="으면 조건",
        level="B1",
        category="조건",
        summary="으면 조건을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="으면 조건은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 으면/면",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="시간이 있으면 같이 가요.",
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
        slug="if-geodeun",
        title="거든요 배경 설명",
        level="B1",
        category="배경",
        summary="거든요 배경 설명을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="거든요 배경 설명은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 거든요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="오늘은 바쁘거든요.",
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
        slug="maybe-euljido-mollayo",
        title="을지도 몰라요 가능성",
        level="B1",
        category="추측",
        summary="을지도 몰라요 가능성을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="을지도 몰라요 가능성은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 을지도/ㄹ지도 몰라요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="길이 막힐지도 몰라요.",
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
        slug="polite-request-a-eo-jusil-su-isseoyo",
        title="아/어 주실 수 있어요 요청",
        level="B1",
        category="요청",
        summary="아/어 주실 수 있어요 요청을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="아/어 주실 수 있어요 요청은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 아/어 주실 수 있어요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="문을 닫아 주실 수 있어요?",
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
        slug="refusal-neun-ge-jom",
        title="완곡한 거절",
        level="B1",
        category="거절",
        summary="완곡한 거절을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="완곡한 거절은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사/명사 + 는 게 좀 어려워요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="오늘 만나는 게 좀 어려워요.",
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
        slug="apology-expressions",
        title="사과 표현",
        level="B1",
        category="화용",
        summary="사과 표현을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="사과 표현은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="죄송하지만/미안하지만 + 설명",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="죄송하지만 오늘은 시간이 없어요.",
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
        slug="contrast-neun-banmyeon",
        title="는 반면에 대조",
        level="B1",
        category="대조",
        summary="는 반면에 대조을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="는 반면에 대조은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 는 반면에",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="도시는 편리한 반면에 복잡해요.",
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
        slug="as-mankeum",
        title="만큼 정도",
        level="B1",
        category="정도",
        summary="만큼 정도을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="만큼 정도은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사/문장 + 만큼",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="연습한 만큼 좋아졌어요.",
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
        slug="nominalizer-gi",
        title="기 명사화",
        level="B1",
        category="명사화",
        summary="기 명사화을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="기 명사화은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사/형용사 어간 + 기",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="한국어를 배우기가 재미있어요.",
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
        slug="cause-neun-baram-e",
        title="는 바람에 원인",
        level="B1",
        category="원인",
        summary="는 바람에 원인을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="는 바람에 원인은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 는 바람에",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="버스를 놓치는 바람에 늦었어요.",
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
        slug="result-ge-dwaesseoyo",
        title="게 됐어요 결과",
        level="B1",
        category="변화",
        summary="게 됐어요 결과을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="게 됐어요 결과은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 게 됐어요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="새 팀에서 일하게 됐어요.",
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
        slug="solution-dorok",
        title="도록 목적",
        level="B1",
        category="목적",
        summary="도록 목적을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="도록 목적은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 도록",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="모두 들을 수 있도록 크게 말해요.",
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
