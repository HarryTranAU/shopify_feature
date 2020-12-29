from main import db
from models.Product import Product
from models.Customer import Customer


class Store(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    storename = db.Column(db.String(), nullable=False, unique=True)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product = db.relationship("Product", backref="store")
    customer = db.relationship("Customer", backref="store")

    def __repr__(self):
        return f"<Store {self.storename}>"
