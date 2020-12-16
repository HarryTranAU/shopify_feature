from models.Store import Store
from models.User import User
from main import db
from schemas.StoreSchema import store_schema, stores_schema
from flask import Blueprint, request, jsonify, abort
from services.auth_service import verify_user
from flask_jwt_extended import jwt_required, get_jwt_identity
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
    pass