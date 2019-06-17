# No doubts api

## Dependencies
    flask, flask_pymongo, flask_jwt_extended

## Config file

Your config.py file should look like this:
```python
  from flask import Flask
  from flask_pymongo import PyMongo
  from flask_jwt_extended import JWTManager

  MONGO_DBNAME = 'atlas_db_name'
  _default_uri = 'atlas_url/'
  MONGO_URI = _default_uri + MONGO_DBNAME

  app = Flask(__name__)
  app.config['MONGO_DBNAME'] = MONGO_DBNAME
  app.config['MONGO_URI'] = MONGO_URI

  app.config['JWT_SECRET_KEY'] = 'YOUR_SECRET_STRING'
  app.config['JWT_BLACKLIST_ENABLED'] = True
  app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

  mongo = PyMongo(app)
  jwt = JWTManager(app)
```