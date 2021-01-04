from main import db
from os import remove
from models.User import User
from schemas.UserSchema import users_schema
from schemas.StoreSchema import stores_schema
from schemas.ProductSchema import products_schema
from schemas.OrderSchema import orders_schema
from schemas.CustomerSchema import customers_schema
from flask import Blueprint, abort
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
import json

admin = Blueprint('admin', __name__)


@admin.route("/admin/backup", methods=["GET"])
@jwt_required
@verify_user
def admin_backup(user):
    user = db.session.query(User)\
                     .filter(User.isAdmin == True)\
                     .filter_by(id=user.id).first()

    if not user:
        return abort(400, description="Unauthorized User")

    try:
        remove("backup.json")
        print("backup removed")
    except FileNotFoundError:
        print("no backup detected")

    tables = ["users", "stores", "products", "customers", "orders"]
    schemas = [users_schema,
               stores_schema,
               products_schema,
               customers_schema,
               orders_schema]

    for table, schema in zip(tables, schemas):
        query = db.engine.execute(f"SELECT * FROM {table}")
        data = json.dumps(schema.dump(query))

        with open("backup.json", "a") as file:
            file.write(data)

    return "OK"
