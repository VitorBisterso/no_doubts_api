from flask import jsonify, request
from bson.objectid import ObjectId
import json

from utils import get_collection, prepare_doubt_output, user_exists

def get_doubts():
  documents = get_collection('doubts')
  output = []
  for document in documents.find({}):
    output.append({
      '_id': str(document['_id']),
      'doubt': document['doubt'],
      'answer': document['answer'],
      'topic': document['topic'],
      'user': document['user'],
    })

  return jsonify(output), 200

def get_doubts_by_user(doubt = 'NONE'):
  user = request.args.get('user')

  query = { 'user': user }
  if doubt == 'NONE':
    query = { 'user': user, 'doubt': doubt }

  if isinstance(user, str):
    if user_exists(user):
      documents = get_collection('doubts')
      output = []
      for document in documents.find(query):
        output.append({
          '_id': str(document['_id']),
          'doubt': document['doubt'],
          'answer': document['answer'],
          'topic': document['topic'],
        })
      return jsonify(output), 200
    else:
      return 'User not found', 404
  else:
    return 'Bad request', 400
      
def get_specific_doubt_from_user():
  doubt = request.args.get('doubt')
  return get_doubts_by_user(doubt)

def create_doubt():
  doubt = request.json.get('doubt')
  answer = request.json.get('answer')
  topic = request.json.get('topic')
  user = request.json.get('user')

  if isinstance(doubt, str) and isinstance(answer, str) and isinstance(topic, str) and isinstance(user, str):
    documents = get_collection('doubts')
    document = {
      'doubt': doubt,
      'answer': answer,
      'topic': topic,
      'user': user,
    }
    document_id = documents.insert(document)

    query = { '_id': document_id }
    inserted_document = documents.find_one(query)
    return prepare_doubt_output(inserted_document), 201
  else:
    return 'Bad request', 400

def update_doubt():
  id = request.args.get('id')

  doubt = request.json.get('doubt')
  answer = request.json.get('answer')
  topic = request.json.get('topic')

  if isinstance(doubt, str) and isinstance(answer, str):
    documents = get_collection('doubts')
    query = { '_id': ObjectId(id) }

    if documents.find_one(query):
      new_values = {'$set': { 'doubt': doubt, 'answer': answer, 'topic': topic } }

      documents.update_one(query, new_values, upsert=True)
      return 'Accepted', 202
    else:
      return 'Doubt not found', 404
  else:
    return 'Bad request', 400

def delete_doubt():
  id = request.args.get('id')

  documents = get_collection('doubts')
  query = { '_id': ObjectId(id) }

  if documents.find_one(query):
    documents.remove(query)
    return 'Accepted', 202
  else:
    return 'Not found', 404

def get_topics_from_user():
  user = request.args.get('user')

  if user_exists(user):
    documents = get_collection('doubts')
    topics = []
    query = { 'user': user }
    for document in documents.find(query):
      if not document['topic'] in topics:
        topics.append(document['topic'])

    return jsonify(topics), 200
  else:
    return 'User not found'

def get_doubts_by_topic_from_user():
  user = request.args.get('user')
  topic = request.args.get('topic')

  if user_exists(user):
    documents = get_collection('doubts')
    output = []
    query = { 'user': user, 'topic': topic }
    for document in documents.find(query):
      output.append({
        '_id': str(document['_id']),
        'doubt': document['doubt'],
        'answer': document['answer'],
        'topic': document['topic'],
        'user': document['user'],
      })

    return jsonify(output), 200
  else:
    return 'User not found'
