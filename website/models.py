from flask_sqlalchemy import model
from flask_login import UserMixin

from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    strategies = db.relationship("Strategy", backref="strategy", cascade="all,delete-orphan")

class Strategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    legs = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))