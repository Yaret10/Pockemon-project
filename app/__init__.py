import os
from flask import Flask
from app.routes.pockemon import pockemon_router
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    app = Flask(__name__)
    app.register_blueprint(pockemon_router)
    return app
