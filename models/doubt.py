from flask import jsonify, request
import json

from utils import get_documents, prepare_doubt_output

def get_doubts():
  documents = get_documents('doubts')
  output = []
  for document in documents.find({}):
    output.append({ 'doubt': document['doubt'], 'answer': document['answer'] })

  return jsonify({ 'result': output }), 200

def get_specific_doubt(doubt):
  documents = get_documents('doubts')
  document = documents.find_one({ 'doubt': doubt })
  if document:
    return prepare_doubt_output(document), 200
  else:
    return 'Not found', 404

def create_doubt():
  doubt = request.json.get('doubt')
  answer = request.json.get('answer')

  if isinstance(doubt, basestring) and isinstance(answer, basestring):
    documents = get_documents('doubts')
    document = {
      'doubt': doubt,
      'answer': answer,
    }
    document_id = documents.insert(document)

    inserted_document = documents.find_one({ "_id": document_id })
    return prepare_doubt_output(inserted_document), 201
  else:
    return 'Bad request', 400
