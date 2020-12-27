import unittest
from main import create_app, db
from models.Product import Product


class TestProducts(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_product_index(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test99@test.com",
                                        "password": "123456"
                                    })

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test99@test.com",
                                        "password": "123456"
                                    })
        data = response.get_json()
        headers_data = {
            'Authorization': f"Bearer {data['token']}"
        }
        data = {
            "storename": "Myteststore",
            "firstname": "testfirst",
            "lastname": "testlast"
        }
        response = self.client.post("/store/",
                                    json=data,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        response = self.client.get(f"/{data['id']}/product/")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_product_create(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test98@test.com",
                                        "password": "123456"
                                    })

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test98@test.com",
                                        "password": "123456"
                                    })
        data = response.get_json()
        headers_data = {
            'Authorization': f"Bearer {data['token']}"
        }
        data = {
            "storename": "Myteststore",
            "firstname": "testfirst",
            "lastname": "testlast"
        }
        response = self.client.post("/store/",
                                    json=data,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        test_product = {
            "title": "testproduct",
            "price": 240
        }
        response = self.client.post(f"/{data['id']}/product/",
                                    json=test_product,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        product = Product.query.get(data['id'])
        self.assertEqual(product.title, "testproduct")
        self.assertEqual(product.price, 240)

    def test_product_update(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test97@test.com",
                                        "password": "123456"
                                    })

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test97@test.com",
                                        "password": "123456"
                                    })
        data = response.get_json()
        headers_data = {
            'Authorization': f"Bearer {data['token']}"
        }
        data = {
            "storename": "Myteststore",
            "firstname": "testfirst",
            "lastname": "testlast"
        }
        response = self.client.post("/store/",
                                    json=data,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        store = response.get_json()
        test_product = {
            "title": "testproduct",
            "price": 240
        }
        response = self.client.post(f"/{store['id']}/product/",
                                    json=test_product,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        product = Product.query.get(data['id'])
        self.assertEqual(product.title, "testproduct")
        self.assertEqual(product.price, 240)

        updated_product = {
            "title": "updatedproduct",
            "price": 1234
        }
        response = self.client.put(f"/{store['id']}/product/{data['id']}",
                                   json=updated_product,
                                   headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        product = Product.query.get(data['id'])
        self.assertEqual(product.title, "updatedproduct")
        self.assertEqual(product.price, 1234)
