from main import ma
from models.Order import Order
from schemas.CustomerSchema import CustomerSchema


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

    order_placed = ma.Boolean()
    customer = ma.Nested(CustomerSchema(only=("email",)))


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
