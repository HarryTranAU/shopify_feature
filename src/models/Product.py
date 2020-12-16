from main import db


class Store(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False, unique=True)
    price = db.Column(db.numeric(), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),
                         nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"
