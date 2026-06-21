"""A1 grammar topics — Korean (ko-KR)."""

from app.data._types import GrammarExample, GrammarMistake, GrammarTopic

A1_GRAMMAR_TOPICS: list[GrammarTopic] = [
    GrammarTopic(
        slug="hangul-basics",
        title="한글 기본",
        level="A1",
        category="문자와 발음",
        summary="한글 기본을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="한글 기본은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="자음 + 모음 = 음절",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="가, 나, 다를 읽고 쓸 수 있어요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="basic-sentence-order",
        title="기본 어순",
        level="A1",
        category="문장 구조",
        summary="기본 어순을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="기본 어순은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="주어 + 목적어 + 서술어",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="저는 물을 마셔요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="imnida-copula",
        title="입니다 명사문",
        level="A1",
        category="명사문",
        summary="입니다 명사문을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="입니다 명사문은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 입니다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="저는 학생입니다.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="eun-neun-topic",
        title="은/는 주제 조사",
        level="A1",
        category="조사",
        summary="은/는 주제 조사을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="은/는 주제 조사은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 은/는",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="저는 마리아예요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="i-ga-subject",
        title="이/가 주어 조사",
        level="A1",
        category="조사",
        summary="이/가 주어 조사을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="이/가 주어 조사은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 이/가",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="비가 와요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="question-intonation",
        title="의문 억양",
        level="A1",
        category="질문",
        summary="의문 억양을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="의문 억양은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="평서문 + 올라가는 억양",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="학생이에요?",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="native-sino-numbers",
        title="고유어 숫자와 한자어 숫자",
        level="A1",
        category="숫자",
        summary="고유어 숫자와 한자어 숫자을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="고유어 숫자와 한자어 숫자은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="하나/둘, 일/이",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="사과 두 개와 물 한 병을 사요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="time-expressions",
        title="시간 표현",
        level="A1",
        category="시간",
        summary="시간 표현을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="시간 표현은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="숫자 + 시/분",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="지금 세 시 십 분이에요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="at-time-e",
        title="시간의 에",
        level="A1",
        category="조사",
        summary="시간의 에을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="시간의 에은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="시간 + 에",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="아침 일곱 시에 일어나요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="isseoyo-eopseoyo",
        title="있어요와 없어요",
        level="A1",
        category="존재",
        summary="있어요와 없어요을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="있어요와 없어요은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 이/가 있어요/없어요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="책상 위에 책이 있어요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="location-e",
        title="장소의 에",
        level="A1",
        category="조사",
        summary="장소의 에을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="장소의 에은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="장소 + 에",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="학교에 친구가 있어요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="demonstratives-i-geu-jeo",
        title="이/그/저 지시어",
        level="A1",
        category="지시 표현",
        summary="이/그/저 지시어을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="이/그/저 지시어은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="이/그/저 + 명사",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="이 가방은 작아요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="ayo-eoyo-present",
        title="아요/어요 현재형",
        level="A1",
        category="동사 활용",
        summary="아요/어요 현재형을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="아요/어요 현재형은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 아요/어요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="저는 매일 공부해요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="object-eul-reul",
        title="을/를 목적격 조사",
        level="A1",
        category="조사",
        summary="을/를 목적격 조사을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="을/를 목적격 조사은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 을/를",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="커피를 마셔요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="daily-action-verbs",
        title="일상 동사",
        level="A1",
        category="동사",
        summary="일상 동사을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="일상 동사은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 현재형",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="아침에 밥을 먹어요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="adjective-present",
        title="형용사 현재형",
        level="A1",
        category="형용사",
        summary="형용사 현재형을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="형용사 현재형은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="형용사 어간 + 아요/어요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="오늘 날씨가 좋아요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="joahaeyo-silheohaeyo",
        title="좋아해요와 싫어해요",
        level="A1",
        category="취향",
        summary="좋아해요와 싫어해요을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="좋아해요와 싫어해요은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 을/를 좋아해요/싫어해요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="저는 음악을 좋아해요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="and-go-connector",
        title="고 연결",
        level="A1",
        category="연결 어미",
        summary="고 연결을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="고 연결은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 고",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="날씨가 좋고 따뜻해요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="juseyo-requests",
        title="주세요 요청",
        level="A1",
        category="요청",
        summary="주세요 요청을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="주세요 요청은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사/동사 어간 + 주세요",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="물 한 잔 주세요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="price-counters",
        title="가격과 단위",
        level="A1",
        category="숫자",
        summary="가격과 단위을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="가격과 단위은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="가격/수량 + 단위",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="사과 세 개에 삼천 원이에요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
    GrammarTopic(
        slug="from-to-eseo-kkaji",
        title="에서와 까지",
        level="A1",
        category="조사",
        summary="에서와 까지을 실제 문장 안에서 자연스럽게 사용할 수 있다.",
        explanation="에서와 까지은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="장소 + 에서 + 장소 + 까지",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="집에서 학교까지 걸어요.",
                translation=None,
                note="자연스러운 사용 예",
            ),
        ],
        common_mistakes=[
            GrammarMistake(
                wrong="문법 형태만 붙여서 어색하게 말하는 경우",
                correct="문장 상황, 조사, 어미, 말투를 함께 확인해서 자연스럽게 쓴다.",
                note="형태 암기보다 실제 문장 안에서의 연결과 높임 정도를 함께 연습합니다.",
            )
        ],
        related=[],
    ),
]
