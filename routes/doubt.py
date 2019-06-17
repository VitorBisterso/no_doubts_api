#Add a config file to run the server
from config import app

from models.doubt import *

@app.route('/doubts', methods=['GET'])
def _get_doubts():
  return get_doubts()

@app.route('/doubts/user', methods=['GET'])
def _get_doubts_by_user():
  return get_doubts_by_user()

@app.route('/doubts/user/doubt', methods=['GET'])
def _get_specific_doubt_from_user():
  return get_specific_doubt_from_user()

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
def _get_topics_from_user():
  return get_topics_from_user()

@app.route('/doubts/topics/user', methods=['GET'])
def _get_doubts_by_topic_from_user():
  return get_doubts_by_topic_from_user()