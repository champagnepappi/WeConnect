from flask import Flask, jsonify, request, session
import re
from app.user_model import User


app = Flask(__name__)
# user = User()
@app.route('/api/v1/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Weconnect'})

@app.route('/api/v1/auth/register', methods=['POST'])
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

    if not username or len(username.strip()) == 0:
        return jsonify({"message": "Username cannot be blank"}),401
    elif not email:
        return jsonify({"message": "Email cannot be blank"}),401
    elif not password:
        return jsonify({"message": "Password cannot be blank"}), 401
    elif password != password_confirmation:
        return jsonify({"message": "Password does not match"}), 401
    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return jsonify({"message": "Input a valid email"}), 401
    elif len(password) < 5:
        return jsonify({"message": "Password too short"}), 401
    elif [u for u in user.users if u['email']== email]:
        return jsonify({"message": "User already exists"}), 401

    user.register_user(username, email, password, password_confirmation)
    return jsonify({"message": "Registration successful"}), 201

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """
    This method checks if user exists in the users list
    then checks if email and password passed matches the ones
    for the list user
    then logs the user in and creates a session
    """
    user_obj = User()
    email = request.json['email']
    password = request.json['password']
    user = [u for u in user_obj.users if email == u['email'] and password == u['password']]
    if  not user:
        return jsonify({"message": "Invalid email/password combination"}), 401

    user_obj.login_user(email, password)
    session['email'] = email
    return jsonify({"message": "Login successful"}), 200

@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """
    This method checks if a session exists
    then logs user out by clearing the session
    """
    user_session = session.get('email')
    if not user_session:
        return jsonify({"message": "You are not logged in"}), 400
    session.pop('email')
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """
    This method checks if user first exists
    then resets the old password and returns a success
    message
    """
    user = User()
    email = request.json['email']
    password = request.json['password']
    password_confirmation = request.json['password_confirmation']
    db_user = [u for u in user.users if email == u['email']]
    if not db_user:
        return jsonify({"message": "Email not found"}), 401
    elif password != password_confirmation:
        return jsonify({"message": "Passwords don't match"}), 401
    elif not password:
        return jsonify({"message": "Password cannot be blank"}), 401
    elif len(password) < 5:
        return jsonify({"message": "Password too short"}), 401
    user.reset_password(email, password, password_confirmation)
    user.user_info['password'] = password
    return jsonify({"message": "Password successfully reset"}), 200






@app.route('/api/v1/users', methods=['GET'])
def get_users():
    user = User()
    return jsonify({'users': user.users})



