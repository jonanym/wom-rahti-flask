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


class Order(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    service = db.Column(db.String, unique=True, nullable=False)
    cabin_id = db.column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    
#with app.app_context():
    #db.create_all()
