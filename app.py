import os
from flask import Flask, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
# create externsion
db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DB_URL')

db.init_app(app)


class Service(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

#with app.app_context():
    #db.create_all()

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

@app.route("/services", methods=['GET', 'POST'])
def services():
    if request.method == 'GET':
        services = []
        for service in Service.query.all():
            services.append({
                'id':service.id,
                'name':service.name,
                'price':service.price,
                'created_at':service.created_at,
                'updated_at':service.updated_at
            })
        return services

    if request.method == 'POST':
        body = request.get_json()
        new_service = Service(name=body['name'], price=body['price'])
        db.session.add(new_service)
        db.session.commit()

        return {'msg: ':'Service created', 'name': new_service.name}

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
