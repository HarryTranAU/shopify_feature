import unittest
from main import create_app, db
from models.Store import Store


class TestStores(unittest.TestCase):
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

    def test_store_index(self):
        response = self.client.get("/store/")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_store_create(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test99@test.com",
                                        "password": "123456",
                                        "isAdmin": False
                                    })

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test99@test.com",
                                        "password": "123456",
                                        "isAdmin": False
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
        store = Store.query.get(data["user"]["id"])
        self.assertIsNotNone(store)
        self.assertEqual(store.storename, "Myteststore")

    def test_store_update(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test98@test.com",
                                        "password": "123456",
                                        "isAdmin": False
                                    })

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test98@test.com",
                                        "password": "123456",
                                        "isAdmin": False
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
        store_data = response.get_json()
        put_data = {
            "storename": "Myupdatedteststore",
            "firstname": "testfirst",
            "lastname": "testlast"
        }
        response = self.client.put(f"/store/{store_data['id']}",
                                   json=put_data,
                                   headers=headers_data)
        data = response.get_json()
        store = Store.query.get(data["id"])
        self.assertEqual(store.storename, "Myupdatedteststore")
        self.assertEqual(response.status_code, 200)

    def test_store_delete(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test97@test.com",
                                        "password": "123456",
                                        "isAdmin": False
                                    })

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test97@test.com",
                                        "password": "123456",
                                        "isAdmin": False
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
        store = Store.query.get(data["user"]["id"])
        self.assertIsNotNone(store)
        self.assertEqual(store.storename, "Myteststore")
        response = self.client.delete(f"/store/{data['user']['id']}",
                                      headers=headers_data)
        self.assertEqual(response.status_code, 200)
