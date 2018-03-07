from flask import Flask, jsonify

app = Flask(__name__)

class User:
    """Demonstrates methods to manipulate user data"""

    def __init__(self):
         self.users = [
         {'user_id': 1, 'name': "Kevin", 'email': "K@gmail.com", 'password': 'pas123'},
         {'user_id': 2, 'name': 'shenin','email': 'jas@gmail.com','password': '1234ab'}
                ]
         self.user_info = {}
         self.user_id = len(self.users)+1

    def register_user(self, username, email, password, password_confirmation):
        if password == password_confirmation:
            self.user_info['user_id'] = self.user_id
            self.user_info['username'] = username
            self.user_info['email'] = email
            self.user_info['password'] = password
            self.users.append(self.user_info)

            return self.user_info
        else:
            return jsonify({'info': 'Password does not match'})

