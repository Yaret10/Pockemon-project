from src.db import db
from sqlalchemy.sql import func


class pockemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    habilidad = db.Column(db.String(100))
    altura = db.Column(db.Integer)

    