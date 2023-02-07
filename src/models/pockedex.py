from src.db import db
from sqlalchemy.sql import func


class pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))