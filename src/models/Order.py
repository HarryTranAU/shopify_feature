from main import db
from models.Product import Product

orders_products = db.Table("orders_products",
                           db.Column("order_id",
                                     db.Integer,
                                     db.ForeignKey("orders.id")),
                           db.Column("product_id",
                                     db.Integer,
                                     db.ForeignKey("products.id")))


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_placed = db.Column(db.Boolean, default=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    orders_products = db.relationship("Product",
                                      secondary=orders_products,
                                      backref="orders")

    def __repr__(self):
        return f"<Order {self.id}, {self.customer_id}>"
