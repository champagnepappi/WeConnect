import unittest
import os
import json
from app import create_app

class UserModelTestCase(unittest.TestCase):
    """This test case represents the user model testcase"""

    def setUp(self):
        """Initialize test varibles"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_hello_there(self):
        response = self.client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client().post('/register',data=json.dumps(
            dict(username="kevin",email="me@gmail.com", password="pass")),
            content_type="application/json")
        self.assertEqual(response.status, 201)

    def test_user_login(self):
        response = self.client().post('/login',data=json.dumps(
             dict(username="kevin", password="pass")),
            content_type="application/json")
        self.assertEqual(response.status, 201)

    def test_user_logout(self):
        response = self.client().post('/api/auth/login',data=json.dumps(
            dict(username="kevin", password="pass")),
            content_type="application/json")
        response = self.client().get('api/auth/logout')
        self.assertEqual(response.status, 200)
