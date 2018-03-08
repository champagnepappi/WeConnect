from flask import Flask, jsonify

app = Flask(__name__)
users = [
    {'user_id': 1, 'name': "Kevin", 'email': "K@gmail.com", 'password': 'pas123'},
    {'user_id': 2, 'name': 'shenin','email': 'jas@gmail.com','password': '1234ab'}
]

class User:
    """Demonstrates methods to manipulate user data"""

    def __init__(self):
        self.user_info = {}
        self.users = users

    def register_user(self, username, email, password, password_confirmation):
        self.user_info['user_id'] = len(self.users)+1

        self.user_info['username'] = username
        self.user_info['email'] = email
        self.user_info['password'] = password
        users.append(self.user_info)
        return self.user_info

