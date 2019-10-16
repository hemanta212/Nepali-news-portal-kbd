"""
contains core routes of webapp
"""

from flask import render_template, redirect, Blueprint, url_for
from flask_login import current_user

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        return redirect(url_for("newslet.nep_national_news"))
    return redirect(url_for("newslet.eng_international_news"))


@main.route("/home", methods=["GET", "POST"])
def homepage():
    return render_template("home.html")


@main.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About this website")


@main.route("/privacy_policy", methods=["GET"])
def privacy_policy():
    return render_template("privacy_policy.html", title="Privacy policy")
