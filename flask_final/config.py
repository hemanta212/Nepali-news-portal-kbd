"""Configurations for the app itself"""
import os
import sys
import json


class Config:

    # basic debuggin properties:
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True  # security for forms

    # whether to detect changes in project
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Email configs for reseting things you know.
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("EMAIL")
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# check if there is a secrets.json file.
def Secrets():
    if os.path.exists("secrets.json"):

        with open("secrets.json", "r") as rf:
            configs = json.load(rf)

        class Config_class(Config):
            SECRET_KEY = configs["SECRET_KEY"]
            MAIL_USERNAME = configs["MAIL_USERNAME"]
            MAIL_PASSWORD = configs["MAIL_PASSWORD"]
            SQLALCHEMY_DATABASE_URI = configs["SQLALCHEMY_DATABASE_URI"]

    return Config_class


class Debug(Config):

    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = (True,)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class SqliteDebug(Debug):
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"


class SqliteProduction(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"


class DatabaseDebug(Debug):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class DatabaseProduction(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
