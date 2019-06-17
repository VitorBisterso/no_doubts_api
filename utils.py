from flask import jsonify

from config import mongo

def get_collection(collection_name):
  return {
    'doubts': mongo.db.doubts,
    'users': mongo.db.users,
  } [collection_name]

def prepare_doubt_output(document):
  output = {
    '_id': str(document['_id']),
    'doubt': document['doubt'],
    'answer': document['answer'],
    'topic': document['topic'],
    'user': document['user'],
  }
  return jsonify({ 'result': output })

def prepare_user_output(document):
  output = {
    '_id': str(document['_id']),
    'user': document['user'],
  }
  return jsonify({ 'result': output })

def user_exists(user):
  documents = get_collection('users')
  query = { 'user': user }
  if documents.find_one(query):
    return True
  
  return False