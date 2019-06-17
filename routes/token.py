from flask import jsonify

from flask_jwt_extended import (
  jwt_required,
  get_jwt_identity,
  create_access_token,
  jwt_refresh_token_required,
  get_raw_jwt
)

from config import app, jwt

blacklist = set()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
  jti = decrypted_token['jti']

  return jti in blacklist

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def _refresh_token():
  current_user = get_jwt_identity()
  access_token = create_access_token(identity = current_user)

  return jsonify({ 'access_token': access_token }), 200

@app.route('/logout/access', methods=['DELETE'])
@jwt_required
def _logout_access():
  jti = get_raw_jwt()['jti']
  blacklist.add(jti)

  return jsonify({ 'message': 'Access token has been revoked' }), 200

@app.route('/logout/refresh', methods=['DELETE'])
@jwt_refresh_token_required
def _logout_refresh():
  jti = get_raw_jwt()['jti']
  blacklist.add(jti)

  return jsonify({ 'message': 'Refresh token has been revoked' }), 200