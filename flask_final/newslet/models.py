from datetime import datetime
from flask_final import db


class NepNationalNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False, )
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    nep_date = db.Column(db.String(20), nullable=False)
    # nep_date = db.Column(db.String(20), nullable = , )
    summary = db.Column(db.Text,)
    title = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text)
    news_link = db.Column(db.Text,)

    def __repr__(self):
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.date)


class NepInternationalNews(db.Model):
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
