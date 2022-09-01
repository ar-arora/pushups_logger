from flask import Blueprint, render_template, url_for

main = Blueprint("main", __name__)

@main.route("/")
def index():

    return render_template("index.html")

@main.route("/profile")
def profile():

    return render_template("profile.html")

@main.route("/user_workouts")
def user_workouts():
    pass

@main.route("/new_workout")
def new_workout():
    pass
