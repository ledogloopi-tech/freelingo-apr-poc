"""Add feedback read states

Revision ID: 0046_feedback_read_states
Revises: 0045_assessment_voice_trial
Create Date: 2026-07-04
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0046_feedback_read_states"
down_revision: str | None = "0045_assessment_voice_trial"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "feedback_read_states",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("entry_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("last_read_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["entry_id"], ["feedback_entries.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("entry_id", "user_id", name="uq_feedback_read_state"),
    )
    op.create_index("ix_feedback_read_states_entry_id", "feedback_read_states", ["entry_id"])
    op.create_index("ix_feedback_read_states_user_id", "feedback_read_states", ["user_id"])


def downgrade() -> None:
    op.drop_index("ix_feedback_read_states_user_id", table_name="feedback_read_states")
    op.drop_index("ix_feedback_read_states_entry_id", table_name="feedback_read_states")
    op.drop_table("feedback_read_states")
