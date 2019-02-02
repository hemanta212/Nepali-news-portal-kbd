<<<<<<< HEAD
import json
=======
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

<<<<<<< HEAD
# for deploying on a linux server use os.environ.get() otherwise
# with open("/etc/kbd/config.json") as json_file:
#    configvar = json.load(json_file)

# disable the warning popup when server starts
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config["SECRET_KEY"] = configvar["SECRET_KEY"]  # use os.environ.get() if not linux server
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
=======
# disable the warning popup when server starts
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
mail = Mail(app)


from flask_final import routes
