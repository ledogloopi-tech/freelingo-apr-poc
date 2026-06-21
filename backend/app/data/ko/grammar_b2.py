"""B2 grammar topics — Korean (ko-KR)."""

from app.data._types import GrammarExample, GrammarMistake, GrammarTopic

B2_GRAMMAR_TOPICS: list[GrammarTopic] = [
    GrammarTopic(
        slug="debate-eun-geon-munje",
        title="는 것이 바람직하다",
        level="B2",
        category="논증",
        summary="는 것이 바람직하다을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="는 것이 바람직하다은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 는 것이 바람직하다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="단계적으로 도입하는 것이 바람직합니다.",
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
        slug="evidence-e-ttareumyeon",
        title="에 따르면 근거",
        level="B2",
        category="근거",
        summary="에 따르면 근거을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="에 따르면 근거은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="자료/출처 + 에 따르면",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="조사에 따르면 이용자가 늘었습니다.",
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
        slug="counterpoint-gineun-hajiman",
        title="기는 하지만 양보",
        level="B2",
        category="양보",
        summary="기는 하지만 양보을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="기는 하지만 양보은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 기는 하지만",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="효과가 있기는 하지만 비용이 큽니다.",
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
        slug="formal-seumnida-che",
        title="습니다체",
        level="B2",
        category="격식체",
        summary="습니다체을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="습니다체은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 습니다/ㅂ니다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="오늘 결과를 발표하겠습니다.",
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
        slug="honorific-si",
        title="시 높임",
        level="B2",
        category="높임",
        summary="시 높임을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="시 높임은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 시",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="선생님께서 오십니다.",
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
        slug="humble-deurida",
        title="드리다 겸양",
        level="B2",
        category="높임",
        summary="드리다 겸양을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="드리다 겸양은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사/동작 + 드리다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="제가 자료를 보내 드리겠습니다.",
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
        slug="supposition-eun-ji-moreuda",
        title="을 것 같다 추측",
        level="B2",
        category="추측",
        summary="을 것 같다 추측을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="을 것 같다 추측은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 을/ㄹ 것 같다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="회의가 길어질 것 같습니다.",
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
        slug="must-eul-teida",
        title="을 테다 예상",
        level="B2",
        category="추측",
        summary="을 테다 예상을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="을 테다 예상은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 을/ㄹ 테다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="지금쯤 도착했을 테예요.",
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
        slug="apparently-na-boda",
        title="나 보다 관찰 추정",
        level="B2",
        category="추측",
        summary="나 보다 관찰 추정을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="나 보다 관찰 추정은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 나 보다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="밖에 비가 오나 봐요.",
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
        slug="cause-eul-tonghae",
        title="으로 인해 원인",
        level="B2",
        category="원인",
        summary="으로 인해 원인을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="으로 인해 원인은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 으로 인해",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="폭우로 인해 행사가 취소되었습니다.",
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
        slug="result-neun-geoya",
        title="는 것이다 설명",
        level="B2",
        category="설명",
        summary="는 것이다 설명을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="는 것이다 설명은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="문장 + 는 것이다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="이 변화는 수요가 늘었다는 것입니다.",
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
        slug="not-only-eul-ppunman-anira",
        title="뿐만 아니라 추가",
        level="B2",
        category="추가",
        summary="뿐만 아니라 추가을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="뿐만 아니라 추가은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사/문장 + 뿐만 아니라",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="시간뿐만 아니라 비용도 줄었습니다.",
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
        slug="nuanced-feelings",
        title="을 수밖에 없다",
        level="B2",
        category="불가피성",
        summary="을 수밖에 없다을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="을 수밖에 없다은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 을/ㄹ 수밖에 없다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="기다릴 수밖에 없었어요.",
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
        slug="regret-eul-geol-geuraetda",
        title="을 걸 그랬다 후회",
        level="B2",
        category="후회",
        summary="을 걸 그랬다 후회을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="을 걸 그랬다 후회은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동사 어간 + 을/ㄹ 걸 그랬다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="미리 예약할 걸 그랬어요.",
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
        slug="while-kin-hande",
        title="기는 한데 완곡 대조",
        level="B2",
        category="대조",
        summary="기는 한데 완곡 대조을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="기는 한데 완곡 대조은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="어간 + 기는 한데",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="좋기는 한데 조금 비싸요.",
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
        slug="definition-ran",
        title="란 정의",
        level="B2",
        category="정의",
        summary="란 정의을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="란 정의은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="명사 + 란",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="문화란 함께 살아가는 방식입니다.",
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
        slug="classification-e-ttara",
        title="에 따라 분류",
        level="B2",
        category="분류",
        summary="에 따라 분류을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="에 따라 분류은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="기준 + 에 따라",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="목적에 따라 표현이 달라집니다.",
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
        slug="academic-eun-bunseok",
        title="학술적 명사화",
        level="B2",
        category="학술 문체",
        summary="학술적 명사화을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="학술적 명사화은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="동작/상태 + 명사형",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="자료의 분석이 필요합니다.",
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
        slug="media-criticism",
        title="보도에 따르면",
        level="B2",
        category="출처",
        summary="보도에 따르면을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="보도에 따르면은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="보도/자료 + 에 따르면",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="보도에 따르면 정책이 바뀔 예정입니다.",
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
        slug="contrast-nevertheless",
        title="그럼에도 불구하고",
        level="B2",
        category="대조",
        summary="그럼에도 불구하고을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="그럼에도 불구하고은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="문장 + 그럼에도 불구하고",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="위험이 있습니다. 그럼에도 불구하고 필요합니다.",
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
        slug="stance-eul-boida",
        title="입장을 보이다",
        level="B2",
        category="태도",
        summary="입장을 보이다을 실제 담화 안에서 자연스럽게 사용할 수 있다.",
        explanation="입장을 보이다은 실제 의사소통에서 자주 쓰이는 문법 항목이다. 형태만 외우기보다 앞뒤 맥락, 말투, 조사와 함께 익히면 자연스럽게 사용할 수 있다.",
        structure="입장/태도 + 을/를 보이다",
        rules=[
            "문장의 상황과 상대에 맞는 말투를 선택한다.",
            "조사와 어미가 앞말의 받침과 품사에 따라 달라지는지 확인한다.",
            "짧은 예문에서 시작해 실제 대화나 글 속 문장으로 확장한다.",
        ],
        examples=[
            GrammarExample(
                text="필자는 신중한 입장을 보입니다.",
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
