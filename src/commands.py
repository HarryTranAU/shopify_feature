from main import db
from flask import Blueprint

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
    from main import bcrypt
    from faker import Faker

    faker = Faker()
    users = []
    stores = []

    for i in range(5):
        user = User()
        user.email = f"test{i+1}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)

    db.session.commit()

    for i in range(5):
        store = Store()

        store.storename = faker.bs()
        store.firstname = faker.first_name()
        store.lastname = faker.last_name()
        store.user_id = users[i].id
        db.session.add(store)
        stores.append(store)

    db.session.commit()

    for i in range(5):
        product = Product()

        product.title = faker.numerify(text="Duck ###")
        product.price = faker.random_int(min=5, max=200, step=5)
        product.store_id = stores[i].id
        db.session.add(product)

    db.session.commit()

    print("Tables seeded")
