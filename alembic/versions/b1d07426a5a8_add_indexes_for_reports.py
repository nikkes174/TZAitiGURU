"""add indexes for reports

Revision ID: b1d07426a5a8
Revises: 56107e2a9862
Create Date: 2026-01-20 08:33:48.336622

"""

from collections.abc import Sequence
from typing import Union

# revision identifiers, used by Alembic.
revision: str = 'b1d07426a5a8'
down_revision: Union[str, Sequence[str], None] = '56107e2a9862'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
