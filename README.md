# Khabar-board
Khabar-board is an online webapp that scrapes news from diffrent new portals of Nepal and worldwide.

Currently, the news is Scraped for National nepali,
International nepali, National english and International english sections from Kantipur and Kathmandu Post, and top headlines from International sources like bbc, cnn, new york times, etc

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
* First properly install python 3.6 or above in your system.
* clone/download this repository and navigate to this repo through cmd
* Run

      python setupenv.py sqlite

             OR

      python setupenv.py postgres

      According to your needs

* Done !!!
* If you are on windows and have problem installing packages try removing gunicorn from requirements.txt.
For manual installation or more details visit [here](https://github.com/hemanta212/Khabar-board/tree/master/docs/manual_install.md)

