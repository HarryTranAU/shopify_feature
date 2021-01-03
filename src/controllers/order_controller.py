from models.Order import Order
from models.Store import Store
from models.Customer import Customer
from models.Product import Product
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
    orders = Order.query.join(Customer)\
                        .join(Store)\
                        .filter(Customer.store_id == storeId).all()
    return jsonify(orders_schema.dump(orders))


@order.route("/<int:customerID>", methods=["POST"])
def order_create(storeId, customerID):
    order_fields = order_schema.load(request.json)

    new_order = Order()
    new_order.order_placed = order_fields["order_placed"]
    cart = order_fields["cart"]
    for item in cart:
        item_query = Product.query.filter_by(id=item).first()
        new_order.orders_products.append(item_query)
        db.session.commit()
    new_order.customer_id = customerID

    customer = Customer.query.filter_by(id=customerID).first()
    if not customer:
        return abort(400, description="Incorrect customer")

    customer.order.append(new_order)
    db.session.commit()

    return jsonify(order_schema.dump(new_order))


@order.route("/delete/<int:orderID>", methods=["DELETE"])
@jwt_required
@verify_user
def order_delete(user, storeId, orderID):
    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    order = Order.query.filter_by(id=orderID).first()
    if not order:
        return abort(400, description="orderID does not exist")

    db.session.delete(order)
    db.session.commit()
    return abort(Response("Order deleted successfully"))


@order.route("/checkout/<int:orderID>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def order_checkout(user, storeId, orderID):
    order_fields = order_schema.load(request.json)

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    order = Order.query.filter_by(id=orderID)
    if not order:
        return abort(400, description="orderID does not exist")

    order.update(order_fields)
    db.session.commit()
    return jsonify(order_schema.dump(order[0]))


@order.route("/sum", methods=["GET"])
@jwt_required
@verify_user
def order_sum(user, storeId):
    pass


@order.route("/abandoned", methods=["GET"])
@jwt_required
@verify_user
def order_abandoned(user, storeId):
    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    orders = Order.query.filter_by(order_placed=False)\
                        .join(Customer)\
                        .join(Store)\
                        .filter(Customer.store_id == storeId)\
                        .all()
    return jsonify(orders_schema.dump(orders))
