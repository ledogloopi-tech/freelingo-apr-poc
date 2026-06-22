from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import JSON, DateTime, Index, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ResourceNativeHelp(Base):
    """Cached native-language help for static learning resources."""

    __tablename__ = "resource_native_helps"

    __table_args__ = (
        UniqueConstraint(
            "resource_type",
            "resource_key",
            "target_language",
            "native_language",
            name="uq_resource_native_helps_resource_lang",
        ),
        Index("ix_resource_native_helps_lookup", "resource_type", "target_language"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    resource_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    resource_key: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    target_language: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    native_language: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    source_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    content: Mapped[dict] = mapped_column(JSON().with_variant(JSONB, "postgresql"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=lambda: datetime.now(UTC).replace(tzinfo=None)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC).replace(tzinfo=None),
        onupdate=lambda: datetime.now(UTC).replace(tzinfo=None),
    )
