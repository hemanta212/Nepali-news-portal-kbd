import os
import tempfile
import pytest
import flask_final

DB_URI = 'SQLALCHEMY_DATABASE_URI'

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    flask_final.app.config['TESTING'] = True
    flask_final.app.config[DB_URI] = 'sqlite:///' + db_path
    client = flask_final.app.test_client()
    flask_final.app.config['WTF_CSRF_ENABLED'] = False
    with flask_final.app.app_context():
        flask_final.db.create_all()
        print("created the database")
    yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_empty_db(client):
    """Start with a blank database."""

    response = client.get('/')
    assert b'Get informed, Get smart' in response.data


def test_try_route(client):

    response = client.get('/try', follow_redirects=True)
    # assert response.status_code == 302
    assert b'Dashboard | Home' in response.data


def login(client, email, password):
    return client.post('/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def signup(client, fullname, email, password):
    return client.post('/signup', data=dict(
        full_name = fullname,
        email = email,
        password = password,
        confirm_password = password
    ), follow_redirects = True)

def test_signup_login(client):
    rv = signup(client, 'aaaa', 'a@b.com', 'sharmaji')
    assert b'Log in' in rv.data


