from bs4 import BeautifulSoup as BS
import requests
import csv
import codecs
import time

count = 0
url = 'http://nagariknews.nagariknetwork.com/category/27'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

page = ''
while page == '' and count < 4:
    try:
        page = requests.get(url, headers=headers)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        count += 1
        print("Was a nice sleep, now let me continue...")
        continue
response = requests.get(url, headers=headers)
soup = BS(response.content, 'lxml')


def nagarik_international_extractor():

    # with codecs.open("ujyaalo_international_cache.csv", "w", encoding='utf-8', errors='ignore') as w:
    # with open("ujyaalo_international_cache.csv", 'w') as w:

    news_articles = soup.find_all('div', class_='detail-on')
    counter = 0
    final_news_list = []

    for news in news_articles:
        title = news.h3.a.text
        date, summary = news.p.text, news.find_all('p')[1].text
        link = "http://nagariknews.nagariknetwork.com" + news.h3.a['href']
        news_dict = {
            'title': title,
<<<<<<< HEAD
            'nep_date': date,
=======
            'date': date,
>>>>>>> 2e3f771e54483475637b5c5ad8eead981285ae7b
            'source': 'Nagarik news',
            'summary': summary,
            'news_link': link,
            'image_link': None
        }
        final_news_list.append(news_dict)
        counter += 1

    # w.write(str(final_news_list))
    return final_news_list


nagarik_international_extractor()
