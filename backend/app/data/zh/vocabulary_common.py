"""Shared helpers for Mainland Chinese vocabulary sets."""

from app.data._types import CEFRLevel, VocabularyEntry, VocabularySet

SetSpec = tuple[str, str, str]


def build_set(level: CEFRLevel, unit_ref: str, spec: SetSpec) -> VocabularySet:
    set_id, topic, headword = spec
    return VocabularySet(
        id=set_id,
        level=level,
        topic=topic,
        unit_ref=unit_ref,
        words=[
            VocabularyEntry(
                word=headword,
                pos="noun",
                definition=f"{topic}话题中的核心词，用于说明人物、事件、观点或场景。",
                example=f"我能在{topic}语境中使用“{headword}”。",
                ipa=None,
                frequency_rank=None,
            ),
            VocabularyEntry(
                word=f"{headword}表达",
                pos="phrase",
                definition=f"在{topic}场景中补充态度、原因或细节的表达。",
                example=f"这个表达可以让{topic}相关句子更具体。",
                ipa=None,
                frequency_rank=None,
            ),
            VocabularyEntry(
                word=f"{headword}句子",
                pos="phrase",
                definition=f"把{topic}词汇连接成完整中文句子的练习表达。",
                example=f"请用自然语序写一个关于{topic}的句子。",
                ipa=None,
                frequency_rank=None,
            ),
        ],
    )
