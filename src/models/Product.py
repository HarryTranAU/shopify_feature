from main import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    price = db.Column(db.Numeric(), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),
                         nullable=False)

    def __repr__(self):
        return f"<Product {self.title}, {self.price}>"
