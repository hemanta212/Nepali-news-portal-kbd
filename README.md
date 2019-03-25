# Khabar-board
(kbd.herokuapp.com)
Khabar-board is an online webapp that scrapes news from diffrent new portals of Nepal. Currently the news is Scraped for National nepali, 
International nepali and National english sections from Kantipur and Kathmandu Post.

It features basic Login and Logout function and email reset function as of now.
It supports Postgresql database as well.
 ## Installation 
 (make it work on your computer)
 
first properly install python 3.6 or above in your system.


step1: clone/download this repository and navigate to this repo through cmd

(optional)
make a virtualenv:

    python -m venv <name>
    
activate it running 
Windows

    Scripts\activate
Linux or Unix
    
    source bin/activate
 
step:2

Now open requirements.txt and remove gunicorn
Then open config.py inside of flask_final and write 'sqlite:///site.db' in place of os.environ.get("DATABASE_URL") and do the same with 
os.environ.get("EMAIL"), os.environ.get("EMAIL_PASSWORD") and write your email and password in strings. In  os.environ.get("SECRET_KEY")
replace it with any random string you like (eg:'jptsrtringkdkfjdlskfjdsfjdkfljdlkfdsjf'). DONE! 

Step3:run 

    pip install -r requirements.txt
then,

    python run.py

