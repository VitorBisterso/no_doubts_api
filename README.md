# No doubts api

## Dependencies
    flask, flask_pymongo

## Config file

Your config.py file should look like this:
```python
  from flask import Flask
  from flask_pymongo import PyMongo

  MONGO_DBNAME = 'atlas_db_name'
  _default_uri = 'atlas_url/'
  MONGO_URI = _default_uri + MONGO_DBNAME

  app = Flask(__name__)
  app.config['MONGO_DBNAME'] = MONGO_DBNAME
  app.config['MONGO_URI'] = MONGO_URI

  mongo = PyMongo(app)
```