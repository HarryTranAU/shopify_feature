from models.Product import Product
from main import db
from schemas.ProductSchema import product_schema, products_schema
from flask import Blueprint, request, jsonify, abort
from services.auth_service import verify_user
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import joinedload

store = Blueprint("stores", __name__, url_prefix="/store")


@store.route("/", methods=["GET"])
def store_index():
    stores = Store.query.options(joinedload("user")).all()
    return jsonify(stores_schema.dump(stores))


@store.route("/", methods=["POST"])
@jwt_required
@verify_user
def store_create(user):
    if user.store != []:
        return abort(400, description="User has already created a store")

    store_fields = store_schema.load(request.json)
    store = Store.query.filter_by(storename=store_fields["storename"]).first()

    if store:
        return abort(400, description="storename already in use")

    new_store = Store()
    new_store.storename = store_fields["storename"]
    new_store.firstname = store_fields["firstname"]
    new_store.lastname = store_fields["lastname"]
    new_store.user_id = user.id

    user.store.append(new_store)
    db.session.commit()

    return jsonify(store_schema.dump(new_store))


@store.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def store_update(user, id):
    store_fields = store_schema.load(request.json)
    store = Store.query.filter_by(id=id, user_id=user.id)

    if not store:
        return abort(400, description="Unauthorized to update this profile")

    print(store.__dict__)
    store.update(store_fields)
    return jsonify(store_schema.dump(store[0]))


@store.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def store_delete(user, id):
    store = Store.query.filter_by(id=id, user_id=user.id).first()

    if not store:
        return abort(400, description="Unauthorized to update this profile")

    db.session.delete(store)
    db.session.commit()
    return jsonify(store_schema.dump(store))