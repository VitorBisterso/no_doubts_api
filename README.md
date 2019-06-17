# No doubts api

## Dependencies
    flask, flask_pymongo, flask_jwt_extended

## Config file

The config.py file uses environment variables. It should look like this:
```python
  from flask import Flask
  from flask_pymongo import PyMongo
  from flask_jwt_extended import JWTManager

  MONGO_DBNAME = os.environ.get('MONGO_DBNAME', default='YOUR_DEFAULT_DB')
  DEFAULT_URI = os.environ.get('DEFAULT_URI', default='YOUR_DEFAULT_URI')
  MONGO_URI = DEFAULT_URI + MONGO_DBNAME

  app = Flask(__name__)
  app.config['MONGO_DBNAME'] = MONGO_DBNAME
  app.config['MONGO_URI'] = MONGO_URI

  app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
  app.config['JWT_BLACKLIST_ENABLED'] = True
  app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

  mongo = PyMongo(app)
  jwt = JWTManager(app)
```