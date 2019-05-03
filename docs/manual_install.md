# Installation

* First properly install python 3.6 or above in your system.

* clone/download this repository and navigate to this repo through cmd

* make a virtualenv:

    python -m venv <name>

Go inside this new folder and activate the virtual environment by running:

For Windows

    Scripts\activate
For Linux or Unix

    source bin/activate

* Now again navigate to Khabar-board folder and rename template_secrets.json to secrets.json

* Run,

    pip install -r requirements.txt
then,

    python manage.py sqlite
    python start.py secrets

* Finally open your browser and head over to http://localhost:5000 and website will load.

* Note: fill secrets.json file with your email and password for password reset functionality!


## Run USING POSTGRES DATABASE.

To run the project on posgres database you need to install postgresql 10+ in your system

* For windows:
Download and install setupfile from https://www.postgresql.org/download/windows/

* Create a postgreql database and obtain its local url
* Now remove the gunicorn in requirements.txt
* then,

      pip install -r requirements.txt

* Add your postgresql local url of database you created earlier to environment variable named DATABASE_URL
* Make new SECRET_KEY environment variable and random string as value

* Note: Add EMAIL and EMAIL_PASSWORD environment variable with your email and password for password reset functionality!

* Finally,
###  If you are setting first time without migrate folder
      python manage.py db init
      python manage.py db migrate
      python manage.py db upgrade
      python manage.py runserver

###  If migrate folder is present
      python manage.py db upgrade
      python manage.py runserver

* For linux:

install postgres:

    sudo apt-get install postgresql postgresql-contrib

* Now create a superuser for PostgreSQL

    sudo -u postgres createuser --superuser name_of_user

* And create a database using created user account

    sudo -u name_of_user createdb name_of_database

* You can access created database with created user by,

    psql -U name_of_user -d name_of_database

* Your postgres database url wil be something like

    postgresql://localhost/name_of_database

* Delete the secrets.json file if present in your folder.

* Set environment variables named DATABASE_URL, EMAIL, and EMAIL_PASSWORD

In linux:

      export DATABASE_URL='postgresql://localhost/name_of_database'
      export EMAIL='your_email@something.com'
      export EMAIL_PASSWORD='your password'

  * Note: EMAIL and EMAIL_PASSWORD are only required for password reset functionality!

* Run

    pip install -r requirements.txt

* After that,

  if migrations folder is present

    python manage.py db upgrade

  otherwise

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

* Finally run the application with.

    python manage.py runserver

* Website will be at http://localhost:5000 load it in your browser.
