from flask import Flask, jsonify, request
from user_model import User

app = Flask(__name__)
user = User()
# users = []

@app.route('/api/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Weconnect'})

@app.route('/auth/register', methods=['POST'])
def register():
    username = request.json['username']
    email  = request.json['email']
    password = request.json['password']
    password_confirmation = request.json['password_confirmation']

    my_user = user.register_user(username, email, password, password_confirmation)
    # users.append(my_user)
    return jsonify(my_user)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': user.users})


# @app.route
# def register():

