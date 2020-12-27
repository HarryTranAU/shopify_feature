from main import ma
from models.Product import Product
from marshmallow.validate import Length, Range
from schemas.StoreSchema import StoreSchema


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

    title = ma.String(required=True, validate=Length(min=1))
    price = ma.Number(required=True, validate=Range(0, 1000000))
    store = ma.Nested(StoreSchema(only=("storename",)))


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
