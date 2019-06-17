#Add a config file to run the server
from config import app

from models.user import *

@app.route('/users', methods=['GET'])
def _is_user_valid():
  return is_user_valid()

@app.route('/users', methods=['POST'])
def _create_user():
  return create_user()
