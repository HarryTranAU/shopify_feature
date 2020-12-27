from models.Product import Product
from models.Store import Store
from main import db
from schemas.ProductSchema import product_schema, products_schema
from flask import Blueprint, request, jsonify, abort, Response
from services.auth_service import verify_user
from flask_jwt_extended import jwt_required

product = Blueprint("products", __name__, url_prefix="/<int:storeId>/product")


@product.route("/", methods=["GET"])
def product_index(storeId):
    products = Product.query.filter_by(store_id=storeId).all()
    return jsonify(products_schema.dump(products))


@product.route("/", methods=["POST"])
@jwt_required
@verify_user
def product_create(user, storeId):
    product_fields = product_schema.load(request.json)
    product = Product.query.filter_by(title=product_fields["title"]).first()
    if product:
        return abort(400, description="Title already in use")

    new_product = Product()
    new_product.title = product_fields["title"]
    new_product.price = product_fields["price"]
    new_product.user_id = user.id

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    store.product.append(new_product)
    db.session.commit()

    return jsonify(product_schema.dump(new_product))


@product.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def product_update(user, storeId, id):
    product_fields = product_schema.load(request.json)
    product = Product.query.filter_by(id=id, store_id=storeId)
    if not product:
        return abort(400, description="Unauthorized to update this product")

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    product.update(product_fields)
    db.session.commit()
    return jsonify(product_schema.dump(product[0]))


@product.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def product_delete(user, storeId, id):
    product = Product.query.filter_by(id=id, store_id=storeId).first()
    if not product:
        return abort(400, description="Unauthorized to delete this product")

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    db.session.delete(product)
    db.session.commit()
    return abort(Response("Product deleted successfully"))
