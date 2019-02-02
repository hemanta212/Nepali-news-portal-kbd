from datetime import datetime
from flask_final import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        '''Gets token for confirming email

        input:
            arg1:optional expires sec(default is 1800 )
        output:
            a serializer token.'''
        s = Serializer(app.config["SECRET_KEY"], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return 'user({0}, {1})'.format(self.full_name, self.email)


class NepNationalNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False, )
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
<<<<<<< HEAD
    nep_date = db.Column(db.String(20), nullable=False)
=======
    # nep_date = db.Column(db.String(20), nullable = , )
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
    summary = db.Column(db.Text,)
    title = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text)
    news_link = db.Column(db.Text,)

    def __repr__(self):
<<<<<<< HEAD
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.date)
=======
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.nep_date)
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b


class NepInternationalNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False, )
<<<<<<< HEAD
    nep_date = db.Column(db.String(20), nullable=False)
=======
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    summary = db.Column(db.Text,)
    title = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text)
    news_link = db.Column(db.Text,)

    def __repr__(self):
<<<<<<< HEAD
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.date)
=======
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.nep_date)
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b


class EngNationalNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False, )
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
<<<<<<< HEAD
    nep_date = db.Column(db.String(20), nullable=False)
=======
    #nep_date = db.Column(db.String(20), nullable = False, )
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
    summary = db.Column(db.Text, )
    title = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text)
    news_link = db.Column(db.Text,)

    def __repr__(self):
<<<<<<< HEAD
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.date)
=======
        return 'news({0}, {1}, {2})'.format(self.id, self.source, self.nep_date)
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
