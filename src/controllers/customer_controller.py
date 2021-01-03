from models.Customer import Customer
from models.Store import Store
from main import db
from schemas.CustomerSchema import customer_schema, customers_schema
from flask import Blueprint, request, jsonify, abort, Response
from services.auth_service import verify_user
from flask_jwt_extended import jwt_required

customer = Blueprint("customers",
                     __name__,
                     url_prefix="/<int:storeId>/customer")


@customer.route("/", methods=["GET"])
@jwt_required
@verify_user
def customer_index(user, storeId):
    customers = Customer.query.filter_by(store_id=storeId).all()

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    return jsonify(customers_schema.dump(customers))


@customer.route("/", methods=["POST"])
@jwt_required
@verify_user
def customer_create(user, storeId):
    customer_fields = customer_schema.load(request.json)
    customer = Customer.query.filter_by(email=customer_fields["email"]).first()
    if customer:
        return abort(400, description="Email already in use")

    new_customer = Customer()
    new_customer.firstname = customer_fields["firstname"]
    new_customer.lastname = customer_fields["lastname"]
    new_customer.email = customer_fields["email"]
    new_customer.phone = customer_fields["phone"]
    new_customer.store_id = storeId

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    store.customer.append(new_customer)
    db.session.commit()

    return jsonify(customer_schema.dump(new_customer))


@customer.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def customer_update(user, storeId, id):
    customer_fields = customer_schema.load(request.json)
    customer = Customer.query.filter_by(id=id, store_id=storeId)
    if not customer:
        return abort(400, description="Unauthorized to update this customer")

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    customer.update(customer_fields)
    db.session.commit()
    return jsonify(customer_schema.dump(customer[0]))


@customer.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def customer_delete(user, storeId, id):
    customer = Customer.query.filter_by(id=id, store_id=storeId).first()
    if not customer:
        return abort(400, description="Unauthorized to delete this customer")

    store = Store.query.filter_by(id=storeId, user_id=user.id).first()
    if not store:
        return abort(400, description="Incorrect storeID in URL")

    db.session.delete(customer)
    db.session.commit()
    return abort(Response("Customer deleted successfully"))
