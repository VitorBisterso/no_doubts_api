from flask_jwt_extended import (
  create_access_token,
  create_refresh_token,
)

from flask import jsonify, request
from bson.objectid import ObjectId
from passlib.hash import sha256_crypt
import json

from utils import get_collection, prepare_user_output

def login():
  user = request.json.get('user')
  password = request.json.get('password')

  query = { 'user': user }
  documents = get_collection('users')
  document = documents.find_one(query)
  if document:
    if sha256_crypt.verify(password, document['password']):
      access_token = create_access_token(identity = document['user'])
      refresh_token = create_refresh_token(identity = document['user'])
      return jsonify({
        'access_token': access_token,
        'refresh_token': refresh_token
      })
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
