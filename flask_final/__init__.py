import json
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_final.config import Config

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

app.config.from_object(Config)
# disable the warning popup when server starts
db = SQLAlchemy(app)
mail = Mail(app)

from flask_final.users.routes import users
from flask_final.newslet.routes import newslet
from flask_final.main.routes import main

app.register_blueprint(users)
app.register_blueprint(newslet)
app.register_blueprint(main)

# for deploying on a linux server use os.environ.get() otherwise
# with open("/etc/kbd/config.json") as json_file:
#    configvar = json.load(json_file)
