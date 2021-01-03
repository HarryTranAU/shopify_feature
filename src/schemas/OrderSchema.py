from main import ma
from models.Order import Order
from schemas.CustomerSchema import CustomerSchema


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

    order_placed = ma.Boolean()
    cart = ma.List(ma.Integer())
    customer = ma.Nested(CustomerSchema(only=("firstname",)))


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
