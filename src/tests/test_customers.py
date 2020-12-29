import unittest
from main import create_app, db
from models.Customer import Customer


class TestCustomers(unittest.TestCase):
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

    def test_customer_index(self):
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
        response = self.client.get(f"/{data['id']}/customer/")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_customer_create(self):
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
        test_customer = {
            "firstname": "testfirstname",
            "lastname": "testlastname",
            "email": "test@emailtest.com",
            "phone": "1234 123 123"
        }
        response = self.client.post(f"/{data['id']}/customer/",
                                    json=test_customer,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        customer = Customer.query.get(data['id'])
        self.assertEqual(customer.firstname, "testfirstname")
        self.assertEqual(customer.lastname, "testlastname")
        self.assertEqual(customer.email, "test@emailtest.com")
        self.assertEqual(customer.phone, "1234 123 123")

    def test_customer_update(self):
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
        test_customer = {
            "firstname": "testfirstname",
            "lastname": "testlastname",
            "email": "test@emailtest.com",
            "phone": "1234 123 123"
        }
        response = self.client.post(f"/{store['id']}/customer/",
                                    json=test_customer,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        customer = Customer.query.get(data['id'])
        self.assertEqual(customer.firstname, "testfirstname")
        self.assertEqual(customer.lastname, "testlastname")
        self.assertEqual(customer.email, "test@emailtest.com")
        self.assertEqual(customer.phone, "1234 123 123")

        updated_customer = {
            "firstname": "changedfirstname",
            "lastname": "changedlastname",
            "email": "changed@emailtest.com",
            "phone": "7896 789 789"
        }
        response = self.client.put(f"/{store['id']}/customer/{data['id']}",
                                   json=updated_customer,
                                   headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        customer = Customer.query.get(data['id'])
        self.assertEqual(customer.firstname, "changedfirstname")
        self.assertEqual(customer.lastname, "changedlastname")
        self.assertEqual(customer.email, "changed@emailtest.com")
        self.assertEqual(customer.phone, "7896 789 789")

    def test_customer_delete(self):
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
        test_customer = {
            "firstname": "testfirstname",
            "lastname": "testlastname",
            "email": "test@emailtest.com",
            "phone": "1234 123 123"
        }
        response = self.client.post(f"/{store['id']}/customer/",
                                    json=test_customer,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        customer = Customer.query.get(data['id'])
        self.assertEqual(customer.firstname, "testfirstname")
        self.assertEqual(customer.lastname, "testlastname")
        self.assertEqual(customer.email, "test@emailtest.com")
        self.assertEqual(customer.phone, "1234 123 123")

        response = self.client.delete(f"/{store['id']}/customer/{data['id']}",
                                      headers=headers_data)
        self.assertEqual(response.status_code, 200)
