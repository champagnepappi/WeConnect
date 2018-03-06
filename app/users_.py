from flask import jsonify, request
from user_model import User

user = User()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Weconnect'})
