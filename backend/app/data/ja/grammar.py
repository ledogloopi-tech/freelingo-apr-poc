"""JA grammar — assembles all CEFR levels."""

from app.data._types import GrammarTopic
from app.data.ja.grammar_a1 import A1_GRAMMAR_TOPICS
from app.data.ja.grammar_a2 import A2_GRAMMAR_TOPICS
from app.data.ja.grammar_b1 import B1_GRAMMAR_TOPICS
from app.data.ja.grammar_b2 import B2_GRAMMAR_TOPICS
from app.data.ja.grammar_c1 import C1_GRAMMAR_TOPICS
from app.data.ja.grammar_c2 import C2_GRAMMAR_TOPICS

GRAMMAR_TOPICS: list[GrammarTopic] = [
    *A1_GRAMMAR_TOPICS,
    *A2_GRAMMAR_TOPICS,
    *B1_GRAMMAR_TOPICS,
    *B2_GRAMMAR_TOPICS,
    *C1_GRAMMAR_TOPICS,
    *C2_GRAMMAR_TOPICS,
]
