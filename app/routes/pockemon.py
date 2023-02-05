from flask import Blueprint
from utils.db import db

pockemon_router = Blueprint('pockemon_router', __name__)

@pockemon_router.route("/")
def index():
    return "hola mundo"