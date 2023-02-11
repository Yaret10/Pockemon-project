import requests
from flask import Blueprint
from flask import request
from flask import render_template, redirect, url_for

from app.databases import db
from app.models.pokemon import Pokemon


pokemon_bp = Blueprint("pokemon", __name__)


POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"


#  *******************************************************
#  ***** Copiado de la BD de Pokemon a la BD MongoDB *****
#  *******************************************************


def retrieve_id():
    url_list = []
    for n in range(0, 41, 20):
        payload = {"offset": n}
        rsp = requests.get(POKEMON_URL, params=payload)
        data_1 = rsp.json()
        url_list += [x["url"] for x in data_1["results"]]

    id_list = []
    for m in url_list:
        rsp = requests.get(m)
        data_2 = rsp.json()
        id_list.append(data_2["id"])

    return id_list


def populate_pokemon(id):
    rsp = requests.get(f"{POKEMON_URL}/{str(id)}")
    data = rsp.json()

    _id = data["id"]
    name = data["name"]
    weight = data["weight"]
    height = data["height"]
    base_experience = data["base_experience"]
    order = data["order"]

    return Pokemon(_id, name, weight, height, base_experience, order)


#  Endpoint: http://127.0.0.1:5000/pokemon/save
@pokemon_bp.route("/pokemon/save", methods=["GET", "POST"])
def save_data():
    if request.method == "POST":
        for id in retrieve_id():
            new_pokemon = populate_pokemon(id)
            db.pokemon.insert_one(new_pokemon.to_json())

        return redirect(url_for("pokemon.get_all"))

    return render_template("pokemon/create-pokemon.html")


#  *************************************************************************
#  *********** Obtención de todos los Pokemones de la BD MongoDB ***********
#  *************************************************************************


#  Endpoint: http://127.0.0.1:5000/pokemon/list
@pokemon_bp.route("/pokemon/list")
def get_all():
    from pymongo import ASCENDING

    pokemon_list = db.pokemon.find().sort("id", ASCENDING)

    return render_template("pokemon/list-pokemon.html", pokemon_list_vw=pokemon_list)


#  *************************************************************************
#  ******* Obtención de todos los Pokemones de la BD MongoDB por ID ********
#  *************************************************************************


#  Endpoint: http://127.0.0.1:5000/pokemon/details/<int:id> --> http://127.0.0.1:5000//pokemon/details/2
@pokemon_bp.route("/pokemon/details/<int:id>", methods=["GET"])
def show_details_id(id):
    found_pokemon = db.pokemon.find_one({"_id": id})

    return render_template("pokemon/details-pokemon.html", obj=found_pokemon)


#  *******************************************************************
#  ** Obtención de todos los Pokemones de la BD MongoDB por NOMBRE ***
#  *******************************************************************


#  Endpoint: http://127.0.0.1:5000/pokemon/details/<string:nombre> --> http://127.0.0.1:5000//pokemon/details/CHARIZARD
@pokemon_bp.route("/pokemon/details/<string:name>", methods=["GET"])
def show_details_name(name):
    name = name.lower()
    found_pokemon = db.pokemon.find_one({"name": name})

    return render_template("pokemon/details-pokemon.html", obj=found_pokemon)