from main import ma
from models.Customer import Customer
from marshmallow.validate import Length
from schemas.StoreSchema import StoreSchema


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

    firstname = ma.String(required=True, validate=Length(min=1))
    lastname = ma.String(required=True, validate=Length(min=1))
    email = ma.String(required=True, validate=Length(min=1))
    phone = ma.String(validate=Length(min=1))
    store = ma.Nested(StoreSchema(only=("storename",)))


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
