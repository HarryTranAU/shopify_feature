from main import ma
from models.Store import Store
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store

    storename = ma.String(validate=Length(min=1))
    firstname = ma.String(validate=Length(min=1))
    lastname = ma.String(validate=Length(min=1))
    user = ma.Nested(UserSchema)


store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)
