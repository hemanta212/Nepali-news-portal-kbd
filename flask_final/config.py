import os

class Config:
    # disable the warning popup when server starts
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # app.config["SECRET_KEY"] = configvar["SECRET_KEY"]
    # use os.environ.get() if not linux server
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
