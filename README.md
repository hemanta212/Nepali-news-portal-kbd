# Khabar-board
Khabar-board is an online webapp that scrapes news from diffrent new portals of Nepal. Currently the news is Scraped for National nepali, 
International nepali and National english sections from Kantipur and Kathmandu Post.

Features:

* Login, Logout, Remember login through cookies
* Reset and confirm email address
* Integrated Unittesting feature
* Scraping of News and serving
* Pagination, Collapsible sidebar, Responsive navigation
* Use proper structure with flask blueprinting
* Support PostgreSQL and Sqlite database
* Hosted Live at heroku @ kbd.herokuapp.com

Todo:
- [ ] Integrate various international news apis
- [ ] Integrate social media login (facebook, github)
- [ ] Use Docker 
- [ ] Add logging
- [ ] Complete testing coverage

## Installation 
 (make it work on your computer)
 
first properly install python 3.6 or above in your system.

step1: clone/download this repository and navigate to this repo through cmd

Step2:
make a virtualenv:

    python -m venv <name>
    
Go inside this new folder and activate the virtual environment by running: 

For Windows

    Scripts\activate
For Linux or Unix
    
    source bin/activate
 

Step3:

Now again navigate to Khabar-board folder and rename template_secrets.json to secrets.json


Step 4:

Run,

    pip install -r bare_requirements.txt
then,

    python manage.py sqlite
    python start.py secrets

Finally open your browser and head over to http://localhost:5000 and website will load.


## Run USING POSTGRES DATABASE.

To run the project on posgres database you need to install postgresql 10+ in your system

* For windows:
Download and install setupfile from https://www.postgresql.org/download/windows/

Create a postgreql database and obtain its local url
Now remove the gunicorn in requirements.txt

then, 
    
      pip install -r requirements.txt

Now, Add your postgresql local url of database you created earlier to environment variable named DATABASE_URL and add random 
strings to a new SECRET_KEY environment variable.

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
