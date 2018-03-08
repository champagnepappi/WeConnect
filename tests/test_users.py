import unittest
import json
from app import create_app

class UserModelTestCase(unittest.TestCase):
    """This test case represents the user model testcase"""

    def setUp(self):
        """Initialize test varibles"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_hello_there(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post('auth/register',data=json.dumps(
            dict(username="kevin",email="me@gmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_user_registering_with_blank_username(self):
        response = self.client.post('auth/register',data=json.dumps(
            dict(username="",email="k@c.com",password="12345",password_confirmation="12345")),
        content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual( "Username cannot be blank", response_msg["message"])

    def test_user_registering_with_blank_email(self):
        response = self.client.post('auth/register',data=json.dumps(
            dict(username="fred",email="",password="12345",password_confirmation="12345")),
        content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual( "Email cannot be blank", response_msg["message"])

    def test_user_registering_with_blank_password(self):
        response = self.client.post('auth/register',data=json.dumps(
            dict(username="fred",email="fred@g.com",password="",password_confirmation="")),
        content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual( "Password cannot be blank", response_msg["message"])

    def test_user_registering_with_wrong_email_format(self):
        response = self.client.post('auth/register',data=json.dumps(
            dict(username="jane",email="megmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Input a valid email", response_msg["message"])

    def test_duplicate_user_registration(self):
        self.client.post('auth/register',data=json.dumps(
            dict(username="jane",email="jane@gmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        response = self.client.post('auth/register',data=json.dumps(
            dict(username="jane",email="jane@gmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User already exists", response_msg["message"])


    def test_user_login(self):
        response = self.client.post('/login',data=json.dumps(
             dict(username="kevin", password="pass")),
            content_type="application/json")
        self.assertEqual(response.status, 201)

    def test_user_logout(self):
        response = self.client.post('/api/auth/login',data=json.dumps(
            dict(username="kevin", password="pass")),
            content_type="application/json")
        response = self.client.get('api/auth/logout')
        self.assertEqual(response.status, 200)
