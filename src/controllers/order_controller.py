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
