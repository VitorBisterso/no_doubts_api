from flask import jsonify, request
import json

from config import mongo

def get_doubts():
  documents = mongo.db.doubts
  output = []
  for document in documents.find({}):
    output.append({ 'doubt': document['doubt'], 'answer': document['answer'] })

  return jsonify({ 'result': output }), 200

def create_doubt():
  doubt = request.json.get('doubt')
  answer = request.json.get('answer')

  if (isinstance(doubt, basestring) and isinstance(answer, basestring)):
    documents = mongo.db.doubts
    document = {
      'doubt': doubt,
      'answer': answer,
    }
    document_id = documents.insert(document)

    inserted_document = documents.find_one({ "_id": document_id })
    output = { 'doubt': inserted_document['doubt'], 'answer': inserted_document['answer'] }
    return jsonify({ 'result': output }), 201
  else:
    return 400
