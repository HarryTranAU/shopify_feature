from models.Order import Order
from models.Store import Store
from main import db
from schemas.OrderSchema import order_schema, orders_schema
from flask import Blueprint, request, jsonify, abort, Response
from services.auth_service import verify_user
from flask_jwt_extended import jwt_required

order = Blueprint("orders",
                  __name__,
                  url_prefix="/<int:storeId>/order")


@order.route("/", methods=["GET"])
def order_index(storeId):
    # orders = Order.query.filter_by(store_id=storeId).all()
    # return jsonify(orders_schema.dump(orders))
    pass


@order.route("/", methods=["POST"])
@jwt_required
@verify_user
def order_create(user, storeId):
    # order_fields = order_schema.load(request.json)
    # order = Order.query.filter_by(email=order_fields["email"]).first()
    # if order:
    #     return abort(400, description="Email already in use")

    # new_order = Order()
    # new_order.firstname = order_fields["firstname"]
    # new_order.lastname = order_fields["lastname"]
    # new_order.email = order_fields["email"]
    # new_order.phone = order_fields["phone"]
    # new_order.store_id = storeId

    # store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    # if not store:
    #     return abort(400, description="Incorrect storeID in URL")

    # store.order.append(new_order)
    # db.session.commit()

    # return jsonify(order_schema.dump(new_order))
    pass


@order.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def order_update(user, storeId, id):
    # order_fields = order_schema.load(request.json)
    # order = Order.query.filter_by(id=id, store_id=storeId)
    # if not order:
    #     return abort(400, description="Unauthorized to update this order")

    # store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    # if not store:
    #     return abort(400, description="Incorrect storeID in URL")

    # order.update(order_fields)
    # db.session.commit()
    # return jsonify(order_schema.dump(order[0]))
    pass


@order.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def order_delete(user, storeId, id):
    # order = Order.query.filter_by(id=id, store_id=storeId).first()
    # if not order:
    #     return abort(400, description="Unauthorized to delete this order")

    # store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    # if not store:
    #     return abort(400, description="Incorrect storeID in URL")

    # db.session.delete(order)
    # db.session.commit()
    # return abort(Response("Order deleted successfully"))
    pass
