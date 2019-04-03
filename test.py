import os
import flask_final
from flask_final.config import SqliteDebug
import unittest
import tempfile

DB_URI = 'SQLALCHEMY_DATABASE_URI'


class TestKbd(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.app = flask_final.create_app(SqliteDebug)
        self.app.config[DB_URI] = 'sqlite:///' + self.db_path
        self.app.testing = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app = self.app.test_client()
        with self.app.app_context():
            flask_final.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_index(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Get informed, Get smart' in response.data)


    def signup(self, full_name='test', email='test@test.com',
        password='test', confirm_password='test'):

        return self.app.post('/signup', data=dict(
            full_name=full_name,
            email=email,
            password=password,
            confirm_password=confirm_password
        ), follow_redirects=True)

    def login(self, email='a@a.com', password='test', remember=True):
        return self.app.post('/login', data=dict(
            email=email,
            password=password,
            remember = remember
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def tryforfree(self):
        return self.app.get('/try', follow_redirects=True)

    def test_signup_login(self):
        '''Test signup and login both here'''

        # Real signup and login
        rv = self.signup(email='a@a.com')
        self.assertTrue(b'Forgot your password?' in rv.data)

        rv = self.login()
        self.assertTrue(b'Dashboard | Home' in rv.data)

        rv = self.logout()
        self.assertTrue(b'Get informed, Get smart' in rv.data)

        # fake signup with already registered email.
        rv = self.signup(email='a@a.com')
        self.assertTrue(b'Email already registered. try another' in rv.data)

        self.tryforfree()
        self.logout()
        rv = self.signup(email='try@try.com')
        self.assertTrue(b'Email already registered' in rv.data)

        # wrong logins with already registered emails.
        rv = self.login(password='wrong')
        self.assertTrue(b'Invalid email or password.' in rv.data)
        rv = self.login(email='try@try.com', password='wrong')
        self.assertTrue(b'Invalid email or password.' in rv.data)

    def test_fake_signups(self):
        '''Signups not dependent on logins'''
        # invalid email
        rv = self.signup(email='sldkjf@dlsaj')
        self.assertTrue(b'Already have an account?' in rv.data)
        # short password length
        rv = self.signup(password='a', confirm_password='a')
        self.assertTrue(b'Field must be at least 3' in rv.data)
        # short full_name
        rv = self.signup(full_name='a')
        self.assertTrue(b'Field must be between 3 and 20' in rv.data)

        # empty password
        rv = self.signup(password=None)
        self.assertTrue(b'Already have an account?' in rv.data)
        rv = self.signup(confirm_password=None)
        self.assertTrue(b'Already have an account?' in rv.data)

        # empty email
        rv = self.signup(email=None)
        self.assertTrue(b'Already have an account?' in rv.data)
        # empty full_name
        rv = self.signup(full_name=None)
        self.assertTrue(b'Already have an account?' in rv.data)

        #password != confirm_password
        rv = self.signup(password='aaaa')
        self.assertTrue(b'Field must be equal to password' in rv.data)

    def test_fake_logins(self):
        # unregistered email
        rv = self.login(email='w@w.com')
        self.assertTrue(b'Invalid email or password.' in rv.data)

        # empty password field
        rv = self.login(password=None)
        self.assertTrue(b'Forgot your password?' in rv.data)

        # empty email field
        rv = self.login(email=None)
        self.assertTrue(b'Forgot your password?' in rv.data)

    def reset_password(self, email):
        return self.app.post('/password/reset', data=dict(
            email=email), follow_redirects=True)

    def test_reset_password(self):
        rv = self.reset_password('wrong@wrong.com')
        self.assertTrue(b'Email not registered. try another' in rv.data)

        # is reset accesible after login?
        self.tryforfree()
        rv = self.reset_password('wrong@wrong.com')
        self.assertTrue(b'Email not registered. try another' in rv.data)

        # test with public try email
        rv = self.reset_password('try@try.com')
        self.assertTrue(b'Invalid request.' in rv.data)


if __name__ == '__main__':
    unittest.main()
