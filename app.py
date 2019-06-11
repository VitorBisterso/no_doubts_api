#Add a config file to run the server
from config import app

from doubt import *

@app.route('/doubts', methods=['GET'])
def _get_doubts():
  return get_doubts()

@app.route('/doubts/<string:doubt>')
def _get_specific_doubt(doubt):
  return get_specific_doubt(doubt)

@app.route('/doubts', methods=['POST'])
def _create_doubt():
  return create_doubt()

@app.route('/doubts/<string:id>', methods=['PUT'])
def _update_doubt(id):
  return update_doubt(id)

@app.route('/doubts/<string:id>', methods=['DELETE'])
def _delete_doubt(id):
  return delete_doubt(id)

@app.route('/doubts/topics', methods=['GET'])
def _get_topics():
  return get_topics()

@app.route('/doubts/topics/<string:topic>', methods=['GET'])
def _get_doubts_by_topic(topic):
  return get_doubts_by_topic(topic)
