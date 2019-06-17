from flask_jwt_extended import jwt_required

#Add a config file to run the server
from config import app

from models.doubt import *

@app.route('/doubts', methods=['GET'])
@jwt_required
def _get_doubts():
  return get_doubts()

@app.route('/doubts/user', methods=['GET'])
@jwt_required
def _get_doubts_by_user():
  return get_doubts_by_user()

@app.route('/doubts/user/doubt', methods=['GET'])
@jwt_required
def _get_specific_doubt_from_user():
  return get_specific_doubt_from_user()

@app.route('/doubts', methods=['POST'])
@jwt_required
def _create_doubt():
  return create_doubt()

@app.route('/doubts/<string:id>', methods=['PUT'])
@jwt_required
def _update_doubt(id):
  return update_doubt(id)

@app.route('/doubts/<string:id>', methods=['DELETE'])
@jwt_required
def _delete_doubt(id):
  return delete_doubt(id)

@app.route('/doubts/topics', methods=['GET'])
@jwt_required
def _get_topics_from_user():
  return get_topics_from_user()

@app.route('/doubts/topics/user', methods=['GET'])
@jwt_required
def _get_doubts_by_topic_from_user():
  return get_doubts_by_topic_from_user()