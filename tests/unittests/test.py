import os
import flask_final
import unittest
import tempfile

DB_URI = 'SQLALCHEMY_DATABASE_URI'


class TestKbd(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        flask_final.app.config[DB_URI] = 'sqlite:///' + self.db_path
        flask_final.app.testing = True
        flask_final.app.config['WTF_CSRF_ENABLED'] = False
        self.app = flask_final.app.test_client()
        with flask_final.app.app_context():
            flask_final.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_index(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Get informed, Get smart' in response.data)

    def signup(self, fullname, email, password):
        return self.app.post('/signup', data=dict(
            full_name=fullname,
            email=email,
            password=password,
            confirm_password=password
        ), follow_redirects=True)

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_signup_login(self):
        '''Test signup and login both here'''

        #Real signup and login
        rv = self.signup('aaaa', 'a@a.com', 'aaaa')
        self.assertTrue(b'Log in' in rv.data)

        rv = self.login('a@a.com', 'aaaa')
        self.assertTrue(b'Dashboard | Home' in rv.data)

        self.logout()
        #fake signup.
        rv = self.signup('fake', 'a@a.com', 'fake')
        self.assertTrue(b'Sign Up' in rv.data)
        # self.assertTrue(b'Email already registered. try another' in rv.data)

    def fake_signups(self):
        '''Signups not dependent on logins'''
        # rv = self.signup('la', ';alskdj', )
        pass



if __name__ == '__main__':
    unittest.main()
