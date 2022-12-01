from flask_sqlalchemy import model
from flask_login import UserMixin

from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    cal_goal = db.Column(db.Float)
    water_goal = db.Column(db.Integer)
    entries = db.relationship("Entry", backref="entry", cascade="all,delete-orphan")
    Water_entries = db.relationship(
        "Water", backref="water", cascade="all,delete-orphan"
    )
