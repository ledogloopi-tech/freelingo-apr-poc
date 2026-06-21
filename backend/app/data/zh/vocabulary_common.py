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
                definition=f"{topic}主题中的核心概念。",
                example=f"我们用中文讨论{topic}。",
                ipa=None,
                frequency_rank=None,
            ),
            VocabularyEntry(
                word=f"{headword}表达",
                pos="phrase",
                definition=f"在{topic}场景中更自然地表达意思。",
                example=f"这个{headword}表达很常用。",
                ipa=None,
                frequency_rank=None,
            ),
            VocabularyEntry(
                word=f"{headword}句子",
                pos="phrase",
                definition=f"把{topic}词汇连接成完整中文句子。",
                example=f"请写一个关于{topic}的句子。",
                ipa=None,
                frequency_rank=None,
            ),
        ],
    )
