from flask import Blueprint
from src.models.pokemon import pockemon


pockemon_router = Blueprint('pockemon_router', __name__)

@pockemon_router.route("/")
def index():
    return "hola mundo"

# @pockemon_router.route("/añadir_datos")
# def index():
#     api_pockemon = "https://pokeapi.co/api/v2/pokemon/"


