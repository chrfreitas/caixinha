from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

import models
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

def create_app():
    db.init_app(app)

    with app.app_context():
        db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, dadasdasd!</p>"

@app.route("/category/<string:name>")
def insert_category(name):
    return "<p>Post</p>"