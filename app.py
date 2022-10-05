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
            'msg': 'Github webhook deployment works!',
            'env': os.environ.get('ENV_VAR', 'Cannot find variable ENV_VAR')
        }
    if request.method == 'POST':
        return{
            'msg': 'You posted something',
        }
    ret = { 
        'msg': 'Flask works on Rahti!', 
        'env': os.environ.get('ENV_VAR', 'Cannot find variable ENV_VAR') 
    }

    return ret


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
