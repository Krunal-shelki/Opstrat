from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
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
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            flash("Logged in successfully!", category="success")
            login_user(user, remember=True)
            return redirect(url_for("views.home"))
        else:
            flash("Incorrect password, Try again!", category="error")
    else:
        flash("User does not exist!", category="error")
    return redirect(url_for("views.home",user=current_user))

@auth.route("/auth/signup", methods=["POST"])
def signup():
    email = request.form.get("s-email")
    password = request.form.get("s-username")
    u_name = request.form.get("s-password")

    new_user = User(
        email = email,
        password = generate_password_hash(password, method="sha256"),
        username = u_name
    )
    db.session.add(new_user)
    db.session.commit()
    print(f'Account Craeted for {email}')
    return redirect(url_for("views.home"))
