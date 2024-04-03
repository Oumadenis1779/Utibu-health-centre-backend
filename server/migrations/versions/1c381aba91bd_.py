"""empty message

Revision ID: 1c381aba91bd
Revises: 
Create Date: 2024-03-28 21:01:15.436999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c381aba91bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('CustomerID', sa.Integer(), nullable=False),
    sa.Column('FirstName', sa.String(length=100), nullable=False),
    sa.Column('LastName', sa.String(length=100), nullable=False),
    sa.Column('Email', sa.String(length=100), nullable=False),
    sa.Column('Phone', sa.String(length=20), nullable=False),
    sa.Column('Address', sa.String(length=255), nullable=True),
    sa.Column('Username', sa.String(length=100), nullable=False),
    sa.Column('Password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('CustomerID')
    )
    op.create_table('medication',
    sa.Column('MedicationID', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=100), nullable=False),
    sa.Column('Description', sa.Text(), nullable=True),
    sa.Column('StockLevel', sa.Integer(), nullable=False),
    sa.Column('PricePerUnit', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('MedicationID')
    )
    op.create_table('orders',
    sa.Column('OrderID', sa.Integer(), nullable=False),
    sa.Column('CustomerID', sa.Integer(), nullable=False),
    sa.Column('OrderDate', sa.DateTime(), nullable=False),
    sa.Column('Status', sa.String(length=20), nullable=False),
    sa.Column('TotalAmount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['CustomerID'], ['customer.CustomerID'], ),
    sa.PrimaryKeyConstraint('OrderID')
    )
    op.create_table('pharmacy_inventory',
    sa.Column('InventoryID', sa.Integer(), nullable=False),
    sa.Column('MedicationID', sa.Integer(), nullable=False),
    sa.Column('Quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['MedicationID'], ['medication.MedicationID'], ),
    sa.PrimaryKeyConstraint('InventoryID')
    )
    op.create_table('statements',
    sa.Column('StatementID', sa.Integer(), nullable=False),
    sa.Column('CustomerID', sa.Integer(), nullable=False),
    sa.Column('StatementDate', sa.DateTime(), nullable=False),
    sa.Column('AmountDue', sa.Float(), nullable=False),
    sa.Column('PaymentStatus', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['CustomerID'], ['customer.CustomerID'], ),
    sa.PrimaryKeyConstraint('StatementID')
    )
    op.create_table('order_items',
    sa.Column('OrderItemID', sa.Integer(), nullable=False),
    sa.Column('OrderID', sa.Integer(), nullable=False),
    sa.Column('MedicationID', sa.Integer(), nullable=False),
    sa.Column('Quantity', sa.Integer(), nullable=False),
    sa.Column('Subtotal', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['MedicationID'], ['medication.MedicationID'], ),
    sa.ForeignKeyConstraint(['OrderID'], ['orders.OrderID'], ),
    sa.PrimaryKeyConstraint('OrderItemID')
    )
    op.create_table('payments',
    sa.Column('PaymentID', sa.Integer(), nullable=False),
    sa.Column('OrderID', sa.Integer(), nullable=False),
    sa.Column('PaymentDate', sa.DateTime(), nullable=False),
    sa.Column('AmountPaid', sa.Float(), nullable=False),
    sa.Column('PaymentMethod', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['OrderID'], ['orders.OrderID'], ),
    sa.PrimaryKeyConstraint('PaymentID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('order_items')
    op.drop_table('statements')
    op.drop_table('pharmacy_inventory')
    op.drop_table('orders')
    op.drop_table('medication')
    op.drop_table('customer')
    # ### end Alembic commands ###
