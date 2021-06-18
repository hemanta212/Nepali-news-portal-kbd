"""Configurations for the app itself"""
import os
import sys
import json


class Prod:
    # basic debuggin properties:
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True  # security for forms

    # whether to detect changes in project
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or ""
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
        # temporary workaround since sqlalchemy has deprecated postgres:// dialect and
        # heroku hasn't updated or allowed users to change the default dialect
        "postgres://",
        "postgresql://",
        1,
    )

    # Email configs for reseting things you know.
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


class Debug(Prod):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = (True,)


# check if there is a secrets.json file.
class Secrets(Debug):
   def __init__(self):
       file = "secrets.json"
       if not os.path.exists(file):
           print(f":: No secrets file {file} found! Exiting..")
           sys.exit(1)
           
       with open(file, "r") as rf:
           print(":: Reading secrets.json file (Only Debug mode suppported!)")
           configs = json.load(rf)

       self.SECRET_KEY = configs["SECRET_KEY"]
       self.MAIL_USERNAME = configs["MAIL_USERNAME"]
       self.MAIL_PASSWORD = configs["MAIL_PASSWORD"]
       self.SQLALCHEMY_DATABASE_URI = configs["SQLALCHEMY_DATABASE_URI"]
       self.NEWS_API_KEY = configs.get("NEWS_API_KEY", "")
