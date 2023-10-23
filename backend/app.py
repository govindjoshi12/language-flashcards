import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

if os.environ['ENV'] == 'prod':
     app.config.from_object('config.ProdConfig')
else:
     app.config.from_object('config.DevConfig')

CORS(app)

from routes import *

if __name__ == "__main__":
     app.run(port=3001)