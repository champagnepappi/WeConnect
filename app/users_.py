from flask import Flask, jsonify, request
import re
from user_model import User


app = Flask(__name__)
# user = User()
@app.route('/api', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Weconnect'})

@app.route('/api/auth/register', methods=['POST'])
def register():
    """
    This methods gets the json data from user
    and uses them to register user with the register_user method
    """
    user = User()
    username = request.json['username']
    email  = request.json['email']
    password = request.json['password']
    password_confirmation = request.json['password_confirmation']

    if not username:
        return jsonify({"message": "Username cannot be blank"})
    elif not email:
        return jsonify({"message": "Email cannot be blank"})
    elif not password:
        return jsonify({"message": "Password cannot be blank"})
    elif password != password_confirmation:
        return jsonify({"message": "Password does not match"})
    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return jsonify({"message": "Input a valid email"})
    elif len(password) < 5:
        return jsonify({"message": "Password too short"})
    elif [u for u in user.users if u['email']== email]:
        return jsonify({"message": "User already exists"})

    my_user = user.register_user(username, email, password, password_confirmation)
    return jsonify(my_user), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    user_obj = User()
    email = request.json['email']
    password = request.json['password']
    user = [u for u in user_obj.users if email == u['email'] and password == u['password']]
    if  not user:
        return jsonify({"message": "Invalid email/password combination"})

    user_obj.login_user(email, password)
    return jsonify({"message": "Login successful"})




@app.route('/users', methods=['GET'])
def get_users():
    user = User()
    return jsonify({'users': user.users})



