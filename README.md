# Khabar-board
Khabar-board is an online webapp that scrapes news from diffrent new portals of Nepal and worldwide.

Currently, the news is Scraped for National nepali,
International nepali, National english and International english sections from Kantipur, Nagarik, Ujyaalo and Kathmandu Post, himalayan times, nepal times and top headlines from International sources like bbc, cnn, new york times, etc

Features:

* Login, Logout, Remember login through cookies
* Reset and confirm email address
* National and International news in both nepali and english
* News collection(scraping, api) and serving
* Pagination, Collapsible sidebar, Responsive navigation
* Use proper structure with flask blueprinting
* Hosted Live at heroku @ kbd.herokuapp.com

Todos:

- [x] Integrate various international news apis(top, general, sports, tech...)
- [x] Rewrite manage.py and database management
- [x] Experiment with docker deploys
- [ ] Add logging
- [ ] Add tests
- [ ] Extract the scraper to separate news API
- [ ] Redesign the dashboard
- [ ] Remove compulsory login and establish per person db record of preferences
- [ ] Give user choice to customize news topic, sources, language etc
- [ ] News search on keyword for custom category (like bitcoin, trump, etc)
- [ ] Integrate social media login (facebook, github)


## Installation and Usage

- Install [python 3.6 or above](https://python.org/downloads)
- Clone/download this repository and navigate to this repo through cmd

```sh
$ git clone https://github.com/hemanta212/nepali-news-portal-kbd
```

- Install either [poetry](https://github.com/python-poetry/poetry) or follow [this guide](/docs/venv.md) for setting up virtual environment.
- Installing dependencies using poetry
```sh
$ poetry install
```
- Installing dependencies using pip.
```sh
$ python -m pip install -r requirements.txt
```

### Setting up Database
You can setup any database supported [here](https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases). This doc covers setting up sqlite and postgres db.

##### Setting up SQLite
Populate the following as your environment variables

```
SECRET_KEY="<your secret key here (random string sequence)"
SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
MAIL_USERNAME="your email",  //optional
MAIL_PASSWORD="your password" //optional
```

###### NOTE
* optional: only required for 'forgot/reset password' functionality to work
If you use gmail and 2 factor-auth, you can use [app passwords](https://support.google.com/accounts/answer/185833) without compromising to low security.

* To enable the international news section get an api key from [News API](https://newsapi.org/register) and set environment variable 'NEWS_API_KEY' to that value.

Alternatively, you can populate these detail in 'template_secrets.json' file and rename it to secrets.json.

##### Setting up the Postgres Databse
The details of installing, configuring a postgres database is [detailed here.](/docs/postgres_setup.md)

Once you have setup the db and have its URI, just set it as the value of 'SQLALCHEMY_DATABASE_URI' in above SQLite section and continue following this doc.

#### Initializing the database
To upgrade the newly created database to the project's structure use 
```
$ python manage.py db upgrade
```

Similarly, if you need to start fresh, delete the migrations folder and now run,
```
$ python manage.py db init # create the migrations folder
$ python manage.py db migrate # create sql commands for the required db construction
$ python manage.py db upgrade # executes those changes in the db
```

#### KNOWN ISSUE
- While Using SQLite relative URI:
Due to the mismatch in the folder level of manage.py and flask application only the sqlite:///site.db relative URI is supported other relative URIs wont work so consider using absolute sqlite URIs.

#### Running the Server
```
    python run.py // production environment (default)
    python run.py debug // for debug environment
```

NOTE: Running in Prod mode is unsupported with secrets.json file and will fallback to Debug.

### Running from gunicorn (Not supported on windows) <a id='gunicorn'></a>
Gunicorn is a production WSGI server that is essential for running flask project in production environments like with Procfile in [Heroku](https://heroku.com).

After installing, you just provide the application instance of project to gunicorn.

eg.
```
gunicorn run:app  // prod env

gunicorn run:app debug
```

#### *NOTE*:
Gunicorn is not supported in windows operating system. However, you can run it using [WSL](https://google.com/search?query=windows%20subsystem%20for%20linux).

## Accessing all news
After successfully running the app, go to localhost:5000/signup and sign up with an account with this admin provisioned email 'try@try.com' (yes this exact email only) and login. You should see news from all the sources.
