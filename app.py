import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        return {
            'method': request.method,
        'msg': 'github webhook works', 
        'env': os.environ.get('ENV_VAR', 'Cannot find variable ENV_VAR')
        }

    if request.method == 'POST':
        body = request.get_json()
        return {
            'msg': 'You POSTed something',
            'request_body': body
        }


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
