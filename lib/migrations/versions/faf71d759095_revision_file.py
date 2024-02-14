"""revision file

Revision ID: faf71d759095
Revises: 36be9d055150
Create Date: 2024-02-14 06:41:04.360655

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, ForeignKey


# revision identifiers, used by Alembic.
revision = 'faf71d759095'
down_revision = '36be9d055150'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('restaurants',
        Column('id', Integer, primary_key=True),
        Column('name', String()),
        Column('price', Integer),
    )

    op.create_table('customers',
        Column('id', Integer, primary_key=True),
        Column('first_name', String()),
        Column('last_name', String()),
    )

    op.create_table('reviews',
        Column('id', Integer, primary_key=True),
        Column('customer_id', Integer, ForeignKey('customers.id')),
        Column('restaurant_id', Integer, ForeignKey('restaurants.id')),
        Column('star_rating', Integer),
    )

    op.create_table('restaurants_customers',
        Column('restaurant_id', Integer, ForeignKey('restaurants.id')),
        Column('customer_id', Integer, ForeignKey('customers.id')),
    )



def downgrade() -> None:
    pass
