import unittest
from main import create_app, db


class TestUsers(unittest.TestCase):
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

    def test_user_register(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test6@test.com",
                                        "password": "123456",
                                        "isAdmin": False
                                    })
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test6@test.com",
                                        "password": "123456",
                                        "isAdmin": False
                                    })
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        response = self.client.post("/user/register",
                                    json={
                                        "email": "test6@test.com",
                                        "password": "123456",
                                        "isAdmin": False
                                    })
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/user/login",
                                    json={
                                        "email": "test1@test.com",
                                        "password": "123456",
                                        "isAdmin": False
                                    })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['token'], str)
