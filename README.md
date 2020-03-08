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
* Support PostgreSQL and Sqlite database
* Hosted Live at heroku @ kbd.herokuapp.com

Todo:
* Tick indcates progress.
- [x] Integrate various international news apis(top, general, sports, tech...)
- [ ] News search on keyword for custom category (like bitcoin, trump, etc)
- [ ] Give user choice to customize news topic, sources, language etc
- [ ] Remove compulsory login and establish per person db record of preferences
- [ ] Redesign the dashboard
- [ ] Integrate social media login (facebook, github)
- [ ] Use Docker
- [x] Add logging
- [x] Add tests
- [ ] Rewrite manage.py and database management

## Installation

### Fast-Track test installation
* First properly install python 3.6 or above in your system.
* clone/download this repository and navigate to this repo through cmd
* Run

      python setupenv.py sqlite

             OR

      python setupenv.py postgres

      According to your needs

* Done !!!

## Note
* If you're facing problems while installing packages in windows try removing the package gunicorn from requirements.txt.

* Also to enable the international news section get an api key from [News API](https://newsapi.org/register) and set environment variable 'NEWS_API_KEY' to that value.

- Once setup completed, You can just activate virtual environment inside venv folder and run ONE of these according to your setup:

```
# For sqlite
    python manage.py sqlite
    python run.py sqlite-prod # Production environment
    python run.py sqlite-debug # Debug environment

# For other databases like postgres, sql
    python run.py db-prod
    python run.py db-debug
```

## Complete installation
For complete installation details visit [installation docs](docs/manual_install.md) which includes:

* Step by step setup process.
* Running with diffrent databases and with debug and production configs

## Accessing all news
After successfully running the app, go to localhost:5000/signup and create an account with this email 'try@try.com' and login. You should see news from all the sources.

