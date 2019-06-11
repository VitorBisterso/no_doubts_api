from flask import jsonify

from config import mongo

def get_collection(collection_name):
  return {
    'doubts': mongo.db.doubts,
  } [collection_name]

def prepare_doubt_output(document):
  output = {
    '_id': str(document['_id']),
    'doubt': document['doubt'],
    'answer': document['answer'],
    'topic': document['topic']
  }
  return jsonify({ 'result': output })