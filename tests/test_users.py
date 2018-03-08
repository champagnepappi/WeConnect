import unittest
import json
from app import create_app

class UserModelTestCase(unittest.TestCase):
    """This test case represents the user model testcase"""

    def setUp(self):
        """Initialize test varibles"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.user = {
            'username': "Krafty",
            'email': "krafty@gmail.com",
            'password': "passwo12",
            'password_confirmation': "passwo12"
        }

    def test_hello_there(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post('/api/auth/register',data=json.dumps(
            dict(username="kevin",email="me@gmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_user_registering_with_blank_username(self):
        response = self.client.post('/api/auth/register',data=json.dumps(
            dict(username="",email="k@c.com",password="12345",password_confirmation="12345")),
        content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual( "Username cannot be blank", response_msg["message"])

    def test_user_registering_with_blank_email(self):
        response = self.client.post('/api/auth/register',data=json.dumps(
            dict(username="fred",email="",password="12345",password_confirmation="12345")),
        content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual( "Email cannot be blank", response_msg["message"])

    def test_user_registering_with_blank_password(self):
        response = self.client.post('/api/auth/register',data=json.dumps(
            dict(username="fred",email="fred@g.com",password="",password_confirmation="")),
        content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual( "Password cannot be blank", response_msg["message"])

    def test_user_registering_with_wrong_email_format(self):
        response = self.client.post('/api/auth/register',data=json.dumps(
            dict(username="jane",email="megmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Input a valid email", response_msg["message"])

    def test_duplicate_user_registration(self):
        self.client.post('/api/auth/register',data=json.dumps(
            dict(username="jane",email="jane@gmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        response = self.client.post('/api/auth/register',data=json.dumps(
            dict(username="jane",email="jane@gmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User already exists", response_msg["message"])


    def test_user_registering_with_passwords_not_matching(self):
        response = self.client.post('/api/auth/register',data=json.dumps(
            dict(username="vim",email="vim@gmail.com", password="pass1",
                 password_confirmation="pass12")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Password does not match", response_msg["message"])


    def test_user_login(self):
        self.client.post('/api/auth/register',data=json.dumps(
            dict(username="kevin",email="me@gmail.com", password="pass12",
                 password_confirmation="pass12")),
            content_type="application/json")
        response = self.client.post('/api/auth/login',data=json.dumps(
             dict(email="me@gmail.com", password="pass12")),
            content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_wrong_user_trying_to_login(self):
        response = self.client.post('/api/auth/login',data=json.dumps(
             dict(email="k@g.com", password="pass12")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Invalid email/password combination", response_msg["message"])
        # self.assertEqual(response.status_code, 200)


    def test_user_logout(self):
        self.client.post('/api/auth/register',data=json.dumps(self.user),
            content_type="application/json")
        self.client.post('/api/auth/login',data=json.dumps(
            dict(email="krafty@gmail.com", password="passwo12")),
            content_type="application/json")
        response = self.client.post('api/auth/logout')
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Logged out successfully", response_msg["message"])
        self.assertEqual(response.status_code, 200)

    def test_user_trying_to_logout_when_not_logged_in(self):
        self.client.post('/api/auth/register',data=json.dumps(self.user),
            content_type="application/json")
        response = self.client.post('api/auth/logout')
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("You are not logged in", response_msg["message"])
        self.assertEqual(response.status_code, 200)

    def test_successful_user_password_reset(self):
        self.client.post('/api/auth/register',data=json.dumps(self.user),
            content_type="application/json")
        self.client.post('/api/auth/login',data=json.dumps(
            dict(email="krafty@gmail.com", password="passwo12")),
            content_type="application/json")
        response = self.client.post('/api/auth/reset-password',data=json.dumps(
            dict(email="krafty@gmail.com",password="12pass",password_confirmation="12pass")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Password successfully reset", response_msg["message"])

    def test_non_existing_user_trying_to_reset_password(self):
        response = self.client.post('/api/auth/reset-password',data=json.dumps(
            dict(email="mais@gmail.com",password="12pass",password_confirmation="12pass")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Email not found", response_msg["message"])

    def test_reseting_password_with_unmatched_passwords(self):
        self.client.post('/api/auth/register',data=json.dumps(self.user),
            content_type="application/json")
        response = self.client.post('/api/auth/reset-password',data=json.dumps(
            dict(email="krafty@gmail.com",password="12232r",password_confirmation="12pass")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Passwords don't match", response_msg["message"])

    def test_reseting_password_with_short_passwords(self):
        self.client.post('/api/auth/register',data=json.dumps(self.user),
            content_type="application/json")
        response = self.client.post('/api/auth/reset-password',data=json.dumps(
            dict(email="krafty@gmail.com",password="122",password_confirmation="122")),
            content_type="application/json")
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Password too short", response_msg["message"])


