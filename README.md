# Khabar-board
Khabar-board is an online webapp that scrapes news from diffrent new portals of Nepal. Currently the news is Scraped for National nepali, 
International nepali and National english sections from Kantipur and Kathmandu Post.

It features basic Login and Logout function and email reset function as of now.
It supports Postgresql database as well.

 ## Installation 
 (make it work on your computer)
 
first properly install python 3.6 or above in your system.


step1: clone/download this repository and navigate to this repo through cmd

Step2(optional):

make a virtualenv:

    python -m venv <name>
    
Go inside this new folder and activate the virtual environment by running: 

For Windows

    Scripts\activate
For Linux or Unix
    
    source bin/activate
 

Step3:

Now open manage.py and flask_final/__init__.py files and in both of them change following lines,
```
from flask_final.config import PosgresProduction as Config
```
To
```
from flask_final.config import SqliteDebug as Config
```
Go to secrets_template.json file and enter your details there and SAVE IT as secrets.json file

Step 4:

Run,

    pip install -r bare_requirements.txt
then,

    python manage.py
    python run.py

Finally open your browser and head over to http://localhost:5000 and website will load.


## Run USING POSTGRES DATABASE.

To run the project on posgres database you need to install postgresql 10+ in your system

For windows:
Download and install setupfile from https://www.postgresql.org/download/windows/

For linux:
install postgres:

    sudo apt-get install postgresql postgresql-contrib
Now create a superuser for PostgreSQL

    sudo -u postgres createuser --superuser name_of_user
And create a database using created user account

    sudo -u name_of_user createdb name_of_database
You can access created database with created user by,
    
    psql -U name_of_user -d name_of_database
    
Your postgres database url wil be "postgresql://localhost/name_of_database"

Delete the secrets.json file if present in your folder.

Now set an environment variable named DATABASE_URL, EMAIL, and EMAIL_PASSWORD

In linux:

      export DATABASE_URL='postgresql://localhost/name_of_database'
      export EMAIL='your_email@something.com'
      export EMAIL_PASSWORD='your password'

Make sure PosgresProduction is imported in manage.py and flask_final/__init__.py files.

Now run

    pip install -r requirements.txt
After that,

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
Finally run the application with.
    
    python manage.py runserver
    
Website will be at http://localhost:5000 load it in your browser. 
