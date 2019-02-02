from bs4 import BeautifulSoup as BS
import requests
import csv
from time import sleep
import codecs


url = 'https://www.kantipurdaily.com/news'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


page = ''
while page == '':
    try:
        page = requests.get(url)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue
soup = BS(page.content, 'lxml')


def kantipur_daily_extractor():
   # with codecs.open("kantipur_daily_cache.csv", "w", encoding='utf-8', errors='ignore') as w:
        # with open("kantipur_daily_cache.csv", 'w') as w:

    counter = 0
    news_list = []
    for article in soup.find_all('article', class_='normal'):

        title = article.h2.a.text
        author = article.find('div', class_='author').text
        summary = article.find('p').text
        date_ore = article.h2.a['href']
        contaminated_list = date_ore.split('/')
        pure_date_list = [contaminated_list[2], contaminated_list[3], contaminated_list[4]]
        date = "/".join(pure_date_list)
        link = "https://kantipurdaily.com" + date_ore
        news_dict = {
            'title': title,
<<<<<<< HEAD
            'nep_date': date,
=======
            'date': date,
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
            'source': 'ekantipur',
            'summary': summary,
            'news_link': link,
            'image_link': None
        }
        news_list.append(news_dict)

        counter += 1
    return news_list


kantipur_daily_extractor()
