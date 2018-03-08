from flask import Flask, jsonify, request
import re
from user_model import User


app = Flask(__name__)
user = User()
@app.route('/api', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Weconnect'})

@app.route('/auth/register', methods=['POST'])
def register():
    username = request.json['username']
    email  = request.json['email']
    password = request.json['password']
    password_confirmation = request.json['password_confirmation']

    if not username or not email or not password or not password_confirmation:
        return jsonify({"message": "Input cannot be blank"})
    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return jsonify({"message": "Input a valid email"})


    my_user = user.register_user(username, email, password, password_confirmation)
    return jsonify(my_user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': user.users})



