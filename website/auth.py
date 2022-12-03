from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import User


auth = Blueprint("auth", __name__)

@auth.route("/auth", methods=["GET"])
def home():
    return render_template("/auth/login_signup.html")

@auth.route("/auth/login", methods=["POST"])
def login():
    email = request.form.get("l-email")
    password = request.form.get("l-password")
    print({
        "u_name" : email,
        "password" : password
    })
    return redirect(url_for("views.home"))

@auth.route("/auth/signup", methods=["POST"])
def signup():
    email = request.form.get("s-email")
    password = request.form.get("s-username")
    u_name = request.form.get("s-password")

    new_user = User(
        email = email,
        password = password,
        username = u_name
    )
    db.session.add(new_user)
    db.session.commit()
    print({
        "email" : email,
        "u_name" : u_name,
        "password" : password,
        "account" : "Created"
    })
    return redirect(url_for("views.home"))
