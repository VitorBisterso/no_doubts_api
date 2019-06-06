from flask import Flask, jsonify
from flask_pymongo import PyMongo

#Add a config.py file to run app.py
from config import MONGO_DBNAME, MONGO_URI

app = Flask(__name__)
app.config['MONGO_DBNAME'] = MONGO_DBNAME
app.config['MONGO_URI'] = MONGO_URI

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def getDoubts():
  doubts = mongo.db.doubts
  output = []
  for doubt in doubts.find({}):
    output.append({ 'doubt': doubt['doubt'], 'answer': doubt['answer'] })

  return jsonify({ 'result': output })

  if __name__ == '__main__':
    app.run(debug=True)