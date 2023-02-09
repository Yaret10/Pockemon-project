from flask import Flask
from app.routes.r_pockemon import pockemon_router
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    app.register_blueprint(pockemon_router)
    return app
