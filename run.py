# import os
# from flask import Flask
# from app.users_ import app
from app import create_app

app = create_app(config_name='development')

if __name__ == '__main__':
    app.run()

