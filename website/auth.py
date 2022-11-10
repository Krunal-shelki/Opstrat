from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/auth", methods=["GET"])
def home():
    return render_template("/auth/login_signup.html")