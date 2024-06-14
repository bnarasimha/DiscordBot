from flask import Flask
from flask import request
import rag

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/getAnswer', methods=['GET'])
def getAnswer():
    query = request.args.get('query')
    return rag.getResponse(query)
    
if __name__ == '__main__':
    app.run()