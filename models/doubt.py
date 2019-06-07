from flask import jsonify, request
from bson.objectid import ObjectId
import json

from utils import get_collection, prepare_doubt_output

def get_doubts():
  documents = get_collection('doubts')
  output = []
  for document in documents.find({}):
    output.append({ '_id': str(document['_id']), 'doubt': document['doubt'], 'answer': document['answer'] })

  return jsonify({ 'result': output }), 200

def get_specific_doubt(doubt):
  documents = get_collection('doubts')
  document = documents.find_one({ 'doubt': doubt })
  if document:
    return prepare_doubt_output(document), 200
  else:
    return 'Not found', 404

def create_doubt():
  doubt = request.json.get('doubt')
  answer = request.json.get('answer')

  if isinstance(doubt, basestring) and isinstance(answer, basestring):
    documents = get_collection('doubts')
    document = {
      'doubt': doubt,
      'answer': answer,
    }
    document_id = documents.insert(document)

    inserted_document = documents.find_one({ '_id': document_id })
    return prepare_doubt_output(inserted_document), 201
  else:
    return 'Bad request', 400

def update_doubt(id):
  doubt = request.json.get('doubt')
  answer = request.json.get('answer')

  if isinstance(doubt, basestring) and isinstance(answer, basestring):
    documents = get_collection('doubts')
    query = { '_id': ObjectId(id) }
    new_values = {'$set': { 'doubt': doubt, 'answer': answer } }

    documents.update_one(query, new_values, upsert=True)
    return 'Accepted', 202
  else:
    return 'Bad request', 400

def delete_doubt(id):
  documents = get_collection('doubts')
  query = { '_id': ObjectId(id) }

  if documents.find_one(query):
    documents.remove(query)
    return 'Accepted', 202
  else:
    return 'Not found', 404
