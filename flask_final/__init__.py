#-*-code: UTF-8
'''
Initialization module of projects that initializes
app, db, Kbdlog,bcrypt, login_manager, mail, Config

'''
import json
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
db = SQLAlchemy()
mail = Mail()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flask_final.users.routes import users
    from flask_final.newslet.routes import newslet
    from flask_final.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(newslet)
    app.register_blueprint(main)

    return app
