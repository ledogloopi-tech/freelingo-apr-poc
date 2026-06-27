"""Add Stripe subscription id to users

Revision ID: 0044_stripe_subscription_id
Revises: 0043_resource_native_helps
Create Date: 2026-06-27
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0044_stripe_subscription_id"
down_revision: str | None = "0043_resource_native_helps"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("users", sa.Column("stripe_subscription_id", sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "stripe_subscription_id")
