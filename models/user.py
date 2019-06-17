from flask import jsonify, request
from bson.objectid import ObjectId
from passlib.hash import sha256_crypt
import json

from utils import get_collection, prepare_user_output

def is_user_valid():
  user = request.json.get('user')
  password = request.json.get('password')

  query = { 'user': user }
  documents = get_collection('users')
  document = documents.find_one(query)
  if document:
    if sha256_crypt.verify(password, sha256_crypt.encrypt(password)):
      return prepare_user_output(document), 200
    else:
      return 'Incorrect password', 401
  else:
    return 'User not found', 404

def create_user():
  user = request.json.get('user')
  password = request.json.get('password')

  documents = get_collection('users')
  query = { 'user': user }
  if not documents.find_one(query):
    if isinstance(user, str) and password:
      encryptedPassword = sha256_crypt.encrypt(password)
      document = {
        'user': user,
        'password': encryptedPassword,
      }
      document_id = documents.insert(document)

      query = { '_id': document_id }
      inserted_document = documents.find_one(query)
      return prepare_user_output(inserted_document), 201
    else:
      return 'Bad request', 400
  else:
    return 'User already exists', 409
