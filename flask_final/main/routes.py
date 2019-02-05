"""
contains core routes of webapp
"""
from flask import render_template, redirect, Blueprint, url_for
from flask_login import current_user
main = Blueprint('main', __name__)


@main.route("/", methods=["GET", 'POST'])
@main.route("/home", methods=["GET", 'POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('newslet.news'))
    return render_template('home.html',)


@main.route("/about", methods=["GET", 'POST'])
def about():
    return render_template('about.html', title="About US")
