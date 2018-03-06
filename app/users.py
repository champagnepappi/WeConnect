from flask import Flask, jsonify

app = Flask(__name__)

class User:

  users = [
       {'id': 1, 'name': "Kevin", 'email': "K@gmail.com", 'password': 'pas123',
        'password_confirmation': 'pas123'  },
           {'id': 2, 'name': 'shenin','email': 'jas@gmail.com','password': '1234ab',
            'password_confirmation': '1234ab'}]

  @app.route('/', methods=['GET'])
  def home():
      return jsonify({'Info': 'Welcome to WeConnect'})


