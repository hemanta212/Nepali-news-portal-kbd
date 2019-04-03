import os
import tempfile
import pytest
import flask_final


@pytest.fixture
def client():
    db_fd, flask_final.app.config['DATABASE'] = tempfile.mkstemp()
    flask_final.app.config['TESTING'] = True
    client = flask_final.app.test_client()

    with flask_final.app.app_context():
        flask_final.db.create_all()
        print("created the database")
    yield client

    os.close(db_fd)
    os.unlink(flask_final.app.config['DATABASE'])

def test_empty_db(client):
    """Start with a blank database."""

    response = client.get('/')
    assert b'Get informed, Get smart' in response.data


def test_try_route(client):

    response = client.get('/try', follow_redirects=True)
    # assert response.status_code == 302
    assert b'Dashboard | Home' in response.data


def login(client, username, password):
    return client.post('/login', data=dict(
        email=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def test_logout(client):
    response = client.get('/try', follow_redirects=True)
    assert b'Dashboard | Home' in response.data
    rv = client.get('/logout', follow_redirects=True)
    assert b'Get informed, Get smart' in response.data


def signup(client, fullname, email, password):
    return client.post('/signup', data=dict(
        Full_Name = fullname,
        email = email,
        password = password,
        confirm_password = password
    ), follow_redirects = True)

# def test_signup(client):
#     # rv = client.get('/signup')
#     rv = login(client, 'try@try.com', 'try')
#     assert b'Dashboard | Home' in rv.data

