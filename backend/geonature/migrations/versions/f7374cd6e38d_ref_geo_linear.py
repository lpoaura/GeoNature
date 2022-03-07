"""ref_geo_linear

Revision ID: f7374cd6e38d
Create Date: 2022-02-25 12:342:56.78

"""
import importlib

from alembic import op, context
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = 'f7374cd6e38d'
down_revision = None
branch_labels = ('ref_geo_linear',)
depends_on = (
    '6afe74833ed0',  # ref_geo
)


def upgrade():
    stmt = text(importlib.resources.read_text('geonature.migrations.data.core', 'ref_geo_linear.sql'))
    op.get_bind().execute(stmt)


def downgrade():
    op.execute('''
        DROP TABLE IF EXISTS ref_geo.cor_linear_group;
        DROP TABLE IF EXISTS ref_geo.t_linear_groups;
        DROP TABLE ref_geo.l_linears;
        DROP TABLE ref_geo.bib_linears_types;
    ''')
