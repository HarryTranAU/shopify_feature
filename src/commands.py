from main import db
from flask import Blueprint
from random import choice

db_commands = Blueprint("db-custom", __name__)


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")


@db_commands.cli.command("seed")
def seed_db():
    from models.User import User
    from models.Store import Store
    from models.Product import Product
    from models.Customer import Customer
    from models.Order import Order, orders_products
    from main import bcrypt
    from faker import Faker

    faker = Faker()
    users = []
    stores = []
    products = []
    customers = []

    for i in range(5):
        user = User()
        user.email = f"test{i+1}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)

        db.session.commit()

        store = Store()
        store.storename = faker.bs()
        store.firstname = faker.first_name()
        store.lastname = faker.last_name()
        store.user_id = users[i].id
        db.session.add(store)
        stores.append(store)

        db.session.commit()

        for j in range(5):
            product = Product()
            product.title = faker.numerify(text="Duck ###")
            product.price = faker.random_int(min=5, max=200, step=5)
            product.store_id = stores[i].id
            db.session.add(product)
            products.append(product)

        db.session.commit()

        for j in range(5):
            customer = Customer()
            customer.firstname = faker.first_name()
            customer.lastname = faker.last_name()
            customer.email = faker.ascii_email()
            customer.phone = faker.phone_number()
            customer.store_id = stores[i].id
            db.session.add(customer)
            customers.append(customer)

            db.session.commit()

            for k in range(5):
                order = Order()
                order.order_placed = choice([True, False])
                order.customer_id = choice(customers).id
                db.session.add(order)

                db.session.commit()

                for m in range(3):
                    order.orders_products.append(choice(products))

                    db.session.commit()

        customers = []

    db.session.commit()

    print("Tables seeded")
