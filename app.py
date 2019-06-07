#Add a config file to run the server
from config import app

#Add a __init__.py inside models folder
from models.doubt import get_doubts, get_specific_doubt, create_doubt

@app.route('/doubts', methods=['GET'])
def _get_doubts():
  return get_doubts()

@app.route('/doubts/<string:doubt>')
def _get_specific_doubt(doubt):
  return get_specific_doubt(doubt)

@app.route('/doubts', methods=['POST'])
def _create_doubt():
  return create_doubt()

if __name__ == '__main__':
  app.run(debug=True)
