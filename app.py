from flask import Flask
from os import environ
from db import db
import models
from flask_smorest import Api
from resources.category import blp as CategoryAPI

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Caixinha REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.1.1"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

    db.init_app(app)
    api = Api(app)

    api.register_blueprint(CategoryAPI)

    with app.app_context():
        db.create_all()
    
    return app

