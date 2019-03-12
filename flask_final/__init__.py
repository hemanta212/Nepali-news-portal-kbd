import json
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_final.config import Config
from logger_file import Logger

class Kbdlog(Logger):
    '''
    A wrapper to logger_file logger for simple unified logging experiance
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dir = "flask_final/logs/"
        self.file = self.dir + self.file
        if self.debug_file:
            self.debug_file = self.dir + self.debug_file


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
