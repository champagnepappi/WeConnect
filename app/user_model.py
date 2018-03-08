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
        """
        This method takes values passed by user and stores them
        in the user_info dict
        Appends the user_info to the users list
        Then returns the user_info
        """
        self.user_info['user_id'] = len(self.users)+1

        self.user_info['username'] = username
        self.user_info['email'] = email
        self.user_info['password'] = password
        users.append(self.user_info)
        return self.user_info


    def login_user(self, email, password):
        """
         This method loops through each user in users lists
         then checks if email and password passed matches the ones
         that exists in the list
         returns user if true and message if false
        """
        for user in users:
            if email == user['email'] and password == user['password']:
                return user
            else:
                return "Wrong email/password combination"

