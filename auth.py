from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/signup")
def signup():

    return "This page is for the User signup"

@auth.route("/login")
def login():

    return "This page is for the User Login"

@auth.route("/logout")
def logout():

    return "This page is for the User Logout"