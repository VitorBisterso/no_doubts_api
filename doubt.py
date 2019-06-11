from flask import jsonify, request
from bson.objectid import ObjectId
import json

from utils import get_collection, prepare_doubt_output

def get_doubts():
  documents = get_collection('doubts')
  output = []
  for document in documents.find({}):
    output.append({
      '_id': str(document['_id']),
      'doubt': document['doubt'],
      'answer': document['answer'],
      'topic': document['topic']
    })

  return jsonify({ 'result': output }), 200

def get_specific_doubt(doubt):
  documents = get_collection('doubts')

  query = { 'doubt': doubt }
  document = documents.find_one(query)
  if document:
    return prepare_doubt_output(document), 200
  else:
    return 'Not found', 404

def create_doubt():
  doubt = request.json.get('doubt')
  answer = request.json.get('answer')
  topic = request.json.get('topic')

  if isinstance(doubt, str) and isinstance(answer, str) and isinstance(topic, str):
    documents = get_collection('doubts')
    document = {
      'doubt': doubt,
      'answer': answer,
      'topic': topic
    }
    document_id = documents.insert(document)

    query = { '_id': document_id }
    inserted_document = documents.find_one(query)
    return prepare_doubt_output(inserted_document), 201
  else:
    return 'Bad request', 400

def update_doubt(id):
  doubt = request.json.get('doubt')
  answer = request.json.get('answer')
  topic = request.json.get('topic')

  if isinstance(doubt, str) and isinstance(answer, str):
    documents = get_collection('doubts')
    query = { '_id': ObjectId(id) }
    new_values = {'$set': { 'doubt': doubt, 'answer': answer, 'topic': topic } }

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

def get_topics():
  documents = get_collection('doubts')
  topics = []
  for document in documents.find({}):
    if not document['topic'] in topics:
      topics.append({ 'topic': document['topic'] })

  return jsonify({ 'result': topics }), 200

def get_doubts_by_topic(topic):
  documents = get_collection('doubts')
  topics = []
  for document in documents.find({}):
    if (not document['topic'] in topics) and (document['topic'] == topic):
      topics.append({
        '_id': str(document['_id']),
        'doubt': document['doubt'],
        'answer': document['answer'],
        'topic': document['topic']
      })

  return jsonify({ 'result': topics }), 200
