# Installation

## Initial Steps
* First properly install python 3.6 or above in your system.
* clone/download this repository and navigate to this repo through cmd

## Installation methods
You can go with either of ways of installation

* [Poetry (Recommended)](#poetry)
    1. [Installing poetry](#set_1)
    2. [Installing packages and running the application](#run_1)

* [Pip and venv (conventional way)](#pip)
    1. [Setting venv](#set_2)
    2. [Installing packages and running the application](#run_2)

## Running with other databases
Running with other databases is simple, you setup any database you like that is supported with flask-sqlalchemy. [See here for supported database list.](https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases) Then you set its URI as a value to ```SQLALCHEMY_DATABASE_URI``` in secrets.json.

You can set every variables present in secrets.json as your environment variables and get rid of secrets.json entirely. [See here for more info](#pg)

* [Running with postgres database](#pg)
  * [Windows setup](#windows_pg)
  * [Unix setup](#unix_pg)

## All ways of running the application
* [Running from manage.py file](#managepy)
* [Running from python and run.py file](#runpy)
* [Running from gunicorn (Not supported on windows)](#gunicorn)


### Poetry <a id='poetry'></a>
[Poetry](https://github.com/python-poetry/poetry) helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere.

#### Installing poetry <a id='set_1'></a>
* [Install poetry](https://github.com/python-poetry/poetry/#installation)

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
Restart the shell.

#### Installing the packages and running project <a id='run_1'></a>
* Rename 'template_secrets.json' to 'secrets.json'.
* Run,
```
poetry install
poetry run python manage.py sqlite
poetry run python run.py secrets
```

* Finally open your browser and head over to http://localhost:5000 and website will load.

##### *Notes*:
- Fill secrets.json file with your email and password for password reset functionality!
- Also, For enabling international news section, get an api from [News api](https://newsapi.org/register) and set environment variable named ```NEWS_API_KEY``` to that token value.


### Pip and venv <a id='pip'></a>
Both pip and venv are provided with the installation of python.
To make sure you have them just go to the cmd prompt and type  and hit enter python -m pip and python -m venv respectively.

#### Setting venv<a id='set_2'></a>

* Make a virtual environment:

```python -m venv venv```
* Activate it
    - For Windows:

    ```venv\Scripts\activate```

    - For Unix:

    ```source venv/bin/activate```

* Rename 'template_secrets.json' to 'secrets.json'.

#### Installing packages and running the application <a id='run_2'></a>
Here we have set the secrets file with necessary configs so we can use it to run. To know about other ways look [here](#runpy).

```
pip install -r requirements.txt
python manage.py sqlite
python run.py secrets
```

* Finally open your browser and head over to http://localhost:5000 and website will load.


##### *Notes*:
- Fill secrets.json file with your email and password for password reset functionality!
- Also, For enabling international news section, get an api from [News api](https://newsapi.org/register) and set environment variable named ```NEWS_API_KEY``` to that token value.


### Run using postgres database. <a id='pg'></a>
To run the project on posgres database you need to install postgresql 10+ in your system

#### Windows setup: <a id='windows_pg'></a>
Download and install [official site](https://www.postgresql.org/download/windows/)

1. Create a postgreql database and obtain its local url
2. Now remove the gunicorn in requirements.txt. Then,

```pip install -r requirements.txt```

3. Add your postgresql local url of database you created earlier to environment variable named ```DATABASE_URL```
4. Make new SECRET_KEY environment variable and random string as value
5. *Note*:
  - Add EMAIL and EMAIL_PASSWORD environment variable with your email and password for password reset functionality!

6. Finally,
* If you are setting first time without migrate folder

```
      python manage.py db init
      python manage.py db migrate
      python manage.py db upgrade
      python manage.py runserver
```
*  If migrate folder is present

```
      python manage.py db upgrade
      python manage.py runserver
```

#### Linux setup: <a id='unix_pg'></a>
1. Install postgres:

```sudo apt-get install postgresql postgresql-contrib```

2. Now create a superuser for PostgreSQL

```sudo -u postgres createuser --superuser name_of_user```

3. And create a database using created user account

```sudo -u name_of_user createdb name_of_database```

4. You can access created database with created user by,

```psql -U name_of_user -d name_of_database```

5. Your postgres database url wil be something like

```postgresql://localhost/name_of_database```

6. Delete the secrets.json file if present in your folder.
7. Set environment variables named DATABASE_URL, EMAIL, and EMAIL_PASSWORD

```
export DATABASE_URL='postgresql://localhost/name_of_database'
export EMAIL='your_email@something.com'
export EMAIL_PASSWORD='your password'
```
7. *Note*:
   -  EMAIL and EMAIL_PASSWORD are optional and only required for password reset functionality!

8. Installation
    * With Poetry ([see installation](#set_1))

    ```poetry install```

    * With Pip

    ```pip install -r requirements.txt```

9. Database Migration
    * If migrations folder is present

    ```python manage.py db upgrade```

    * Otherwise,
    ```
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```

10. Running.

```python manage.py runserver```

* Website will be at http://localhost:5000 load it in your browser.


## All ways of running the application
### Running from manage.py file <a id='managepy'></a>
The 'manage.py' is the single file to manage your project. It will help you handle db migrations, db inits and run the project itself. It is the general convention in python web projects to have a 'manage.py' (or similar) file.

The way I have set this up is  runserver command will run the production version of app reading configs from environment variables.

```python manage.py runserver```

This is production settings and if you need to run other configuration then ['run.py'](#runpy) is best method

### Running from python and run.py file <a id='runpy'></a>
'run.py' is a custom python file to run the project with diffrent configurations.
You specify the configuration type as arguments and then it will run the app.

```python run.py <CONFIG_NAME>```

* Configuration types are.
- sqlite-debug
- sqlite-prod
- database-prod
- database-debug
- secrets (reads config from secrets.json file)

eg.

```python run.py sqlite-debug```

If no arguments is provided the default configuration is set as Database production which reads every config from environment variable

This run.py script is used while deploying in platfroms like heroku. Where gunicorn calls this run.py script. See [gunicorn](#gunicorn) for more info.

### Running from gunicorn (Not supported on windows) <a id='gunicorn'></a>
Gunicorn is a production WSGI server that is essential for running flask project in production mode.

After installing, you just provide the application instance of project to gunicorn.

eg.
```
gunicorn run:app #uses default config of run.py
gunicorn run:app sqlite-debug
gunicorn run:app database-debug
```

#### *NOTE*:
Gunicorn is not supported in windows operating system. You can run it on [WSL](https://google.com/search?query=windows%20subsytem%20for%20linux) however.
