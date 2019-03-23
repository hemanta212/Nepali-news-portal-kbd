'''
Database models for storing news
Contains 3 classes:
    NepNationalNews: national news in nepali database model
    NepInternationalNews : international news in nepali  database model
    EngNationalNews :National news in english database model
'''
from datetime import datetime
from flask_final import db


class NepNationalNews(db.Model):
    '''
    Provides date(model created), id atrribute by default
    Initialize with compulsory
        source : news source like 'ekantipur'
        nep_date: date provided by the website itself
        summary : news summary
        title : title of the news
    Optional initialization
        image_link
        news_link
    '''
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False, )
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    nep_date = db.Column(db.String(20), nullable=False)
    summary = db.Column(db.Text,)
    title = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text)
    news_link = db.Column(db.Text,)

    def __repr__(self):
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.date)


class NepInternationalNews(db.Model):
    '''
    Provides date(model created), id atrribute by default
    Initialize with compulsory
        source : news source like 'ekantipur'
        nep_date: date provided by the website itself
        summary : news summary
        title : title of the news
    Optional initialization
        image_link
        news_link
    '''

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False, )
    nep_date = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    summary = db.Column(db.Text,)
    title = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text)
    news_link = db.Column(db.Text,)

    def __repr__(self):
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.date)


class EngNationalNews(db.Model):
    '''
    Provides date(model created), id atrribute by default
    Initialize with compulsory
        source : news source like 'ekantipur'
        nep_date: date provided by the website itself
        summary : news summary
        title : title of the news
    Optional initialization
        image_link
        news_link
    '''

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False, )
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    nep_date = db.Column(db.String(20), nullable=False)
    summary = db.Column(db.Text, )
    title = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text)
    news_link = db.Column(db.Text,)

    def __repr__(self):
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.date)
