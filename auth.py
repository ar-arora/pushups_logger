from flask import Blueprint, render_template, url_for, request, redirect
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

auth = Blueprint("auth", __name__)


@auth.route("/signup")
def signup():

    return render_template("signup.html")

@auth.route("/signup", methods = ["POST"])
def signup_post():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    print("Entered : ", name, email, password)

    user = User.query.filter_by(email = email).first()

    if user:
        print("User with email : {} already exists...".format(email))

    new_user = User(name = name, email = email, password = generate_password_hash(password, method = "sha256"))
    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for("auth.login"))


@auth.route("/login")
def login():

    return render_template("login.html")

@auth.route("/login", methods = ["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email = email).first()

    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))

    login_user(user, remember= remember)

    return redirect(url_for("main.profile"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))