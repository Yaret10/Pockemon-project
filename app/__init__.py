from flask import Flask

from app.routes.principal_router import principal_bp
from app.routes.pokemon_router import pokemon_bp
from app.routes.pokedex_router import pokedex_bp

def create_app() -> Flask :

    app= Flask(__name__)

    app.register_blueprint(principal_bp)
    app.register_blueprint(pokemon_bp)
    app.register_blueprint(pokedex_bp)

    return app
