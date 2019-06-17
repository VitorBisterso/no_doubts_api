# No doubts api

## Dependencies
    flask, flask_pymongo, flask_jwt_extended

## Config file

The config.py file uses environment variables. It should look like this:
```python
  import os

  from flask import Flask
  from flask_pymongo import PyMongo
  from flask_jwt_extended import JWTManager

  MONGO_URI = os.environ.get('MONGO_URI')

  app = Flask(__name__)
  app.config['MONGO_URI'] = MONGO_URI

  app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
  app.config['JWT_BLACKLIST_ENABLED'] = True
  app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

  mongo = PyMongo(app)
  jwt = JWTManager(app)
```