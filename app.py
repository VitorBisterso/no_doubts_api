#Add a config file to run the server
from config import app

#Add a __init__.py inside models folder
from models.doubt import get_doubts, create_doubt

@app.route('/doubts', methods=['GET'])
def get():
  return get_doubts()

@app.route('/doubts', methods=['POST'])
def post():
  return create_doubt()

if __name__ == '__main__':
  app.run(debug=True)
