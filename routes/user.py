from config import app

from models.user import *

@app.route('/login', methods=['POST'])
def _login():
  return login()

@app.route('/sign_up', methods=['POST'])
def _create_user():
  return create_user()
