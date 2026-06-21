"""Shared helpers for Mainland Chinese grammar topics."""

from app.data._types import CEFRLevel, GrammarExample, GrammarTopic

TopicSpec = tuple[str, str, str, str, str]


def build_topic(level: CEFRLevel, spec: TopicSpec) -> GrammarTopic:
    slug, title, category, structure, example = spec
    return GrammarTopic(
        slug=slug,
        title=title,
        level=level,
        category=category,
        summary=f"学习{title}，能在{level}阶段更准确地理解和表达中文。",
        explanation=(
            f"{title}是现代汉语中常见的语法项目。学习时要结合语境、语序、词语搭配和语气，"
            "不要只记形式，要在真实句子中练习使用。"
        ),
        structure=structure,
        rules=[
            "注意中文基本语序和前后成分的搭配。",
            "根据语境判断语气、时间和信息重点。",
            "先用短句练习，再扩展到对话和段落。",
        ],
        examples=[GrammarExample(text=example, note="自然用法示例")],
        common_mistakes=[],
        related=[],
    )
