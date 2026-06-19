"""Add reviews table

Revision ID: 0042_reviews
Revises: 0041_backfill_learning_goals
Create Date: 2026-06-19
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0042_reviews"
down_revision: str | None = "0041_backfill_learning_goals"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "reviews",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("user_display_name", sa.String(length=150), nullable=False),
        sa.Column("target_language", sa.String(length=10), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("comment", sa.Text(), nullable=True),
        sa.Column("is_approved", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.CheckConstraint("rating >= 1 AND rating <= 5", name="ck_reviews_rating_range"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", name="uq_reviews_user_id"),
    )
    op.create_index("ix_reviews_user_id", "reviews", ["user_id"])
    op.create_index("ix_reviews_target_language", "reviews", ["target_language"])
    op.create_index("ix_reviews_is_approved", "reviews", ["is_approved"])
    op.create_index("ix_reviews_created_at", "reviews", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_reviews_created_at", table_name="reviews")
    op.drop_index("ix_reviews_is_approved", table_name="reviews")
    op.drop_index("ix_reviews_target_language", table_name="reviews")
    op.drop_index("ix_reviews_user_id", table_name="reviews")
    op.drop_table("reviews")
