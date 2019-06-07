from flask import jsonify

from config import mongo

def get_collection(collection_name):
  return {
    'doubts': mongo.db.doubts,
  } [collection_name]

def prepare_doubt_output(document):
  output = { 'doubt': document['doubt'], 'answer': document['answer'] }
  return jsonify({ 'result': output })