import requests
from flask import Blueprint
from flask import request
from flask import render_template, redirect, url_for

from app.databases import db
from app.models.pokedex import Pokedex


pokedex_bp = Blueprint("pokedex", __name__)


POKEDEX_URL = "https://pokeapi.co/api/v2/pokedex/"
LIST_POKEDEX = "pokedex/list-pokedex.html"


#  *************************************************************************
#  ************** Copiado de la BD de Pokedex a la BD MongoDB **************
#  *************************************************************************


def retrieve_id():
    url_list = []
    for n in range(0, 51, 20):
        payload = {"offset": n}
        rsp = requests.get(POKEDEX_URL, params=payload)
        data_1 = rsp.json()
        url_list += [x["url"] for x in data_1["results"]]

    id_list = []
    for m in url_list:
        rsp = requests.get(m)
        data_2 = rsp.json()
        id_list.append(data_2["id"])
    
    return id_list


def populate_pokedex(id):
    rsp = requests.get(f"{POKEDEX_URL}/{str(id)}")
    data = rsp.json()

    _id = data["id"]
    name = data["name"]

    descriptions_list = []
    for d in data["descriptions"]:
        if d["description"] == "":
            descriptions_list.append("EMPTY")
            break
        descriptions_list.append(d["description"])

    descriptions = ", ".join(descriptions_list)

    return Pokedex(_id, name, descriptions)


#  Endpoint: http://127.0.0.1:5000/pokedex/save
@pokedex_bp.route("/pokedex/save", methods=["GET", "POST"])
def save_data():
    if request.method == "POST":
        for id in retrieve_id():
            new_pokedex = populate_pokedex(id)
            db.pokedex.insert_one(new_pokedex.to_json())

        return redirect(url_for("pokedex.get_all"))

    return render_template("pokedex/create-pokedex.html")


#  *************************************************************************
#  ************ Obtención de todos los Pokedex de la BD MongoDB ************
#  *************************************************************************


#  Endpoint: http://127.0.0.1:5000/pokedex/list
@pokedex_bp.route("/pokedex/list")
def get_all():
    from pymongo import ASCENDING

    pokedex_list = db.pokedex.find().sort("id", ASCENDING)

    return render_template(LIST_POKEDEX, pokedex_list_vw=pokedex_list)


#  *************************************************************************
#  ******* Obtención de todos los Pokedex de la BD MongoDB por ID ********
#  *************************************************************************


#  Endpoint: http://127.0.0.1:5000/pokedex/list/<int:id> --> http://127.0.0.1:5000//pokedex/list/1
@pokedex_bp.route("/pokedex/details/<int:id>", methods=["GET"])
def show_details_id(id):
    found_pokedex = db.pokedex.find_one(id)

    return render_template("pokedex/details-pokedex.html", obj=found_pokedex)


#  *************************************************************************
#  ****** Obtención de todos los Pokedex de la BD MongoDB por NOMBRE *******
#  *************************************************************************


#  Endpoint: http://127.0.0.1:5000/pokedex/list/<string:nombre> --> http://127.0.0.1:5000//pokedex/list/ORIGINAL-ULAULA
@pokedex_bp.route("/pokedex/details/<string:name>", methods=["GET"])
def show_details_name(name):
    name = name.lower()
    found_pokedex = db.pokedex.find_one({"name": name})

    return render_template("pokedex/details-pokedex.html", obj=found_pokedex)