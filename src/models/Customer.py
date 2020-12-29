from main import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    phone = db.Column(db.String())
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),
                         nullable=False)

    def __repr__(self):
        return f"<Customer {self.firstname}, {self.lastname}, {self.email}>"
