from flask import Flask, jsonify

app = Flask(__name__)

class User:

  @app.route('/', methods=['GET'])
  def home():
      return jsonify({'Info': 'Welcome to WeConnect'})
