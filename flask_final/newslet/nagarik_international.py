from bs4 import BeautifulSoup as BS
import requests


url = 'http://nagariknews.nagariknetwork.com/category/27'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

try:
    page = requests.get(url, headers=headers)
except Exception as e:
    print("Connection refused by the server..", e)

response = requests.get(url, headers=headers)
soup = BS(response.content, 'lxml')


def nagarik_international_extractor():

    # with codecs.open("ujyaalo_international_cache.csv", "w",
    #  encoding='utf-8', errors='ignore') as w:
    # with open("ujyaalo_international_cache.csv", 'w') as w:
    def cover_news(nep_date):
        cover_news_list = []
        cover_div = soup.find_all("div", class_='col-sm-3 part-ent')
        for news in cover_div:
            image_url = news.div.img['src']
            title = news.h3.a.text
            summary = news.p.text
            primary_url = "https://nagariknews.nagariknetwork.com"
            news_link = primary_url + news.h3.a['href']
            cover_news_dict = {
                'title': title,
                'summary': summary,
                'source': 'Nagarik news',
                'summary': summary,
                'news_link': news_link,
                'image_link': image_url,
                'nep_date': nep_date,
            }
            cover_news_list.append(cover_news_dict)
        return cover_news_list

    news_articles = soup.find_all('div', class_='detail-on')
    counter = 0
    main_news_list = []

    for news in news_articles:
        title = news.h3.a.text
        date, summary = news.p.text, news.find_all('p')[1].text
        link = "http://nagariknews.nagariknetwork.com" + news.h3.a['href']
        news_dict = {
            'title': title,
            'nep_date': date,
            'source': 'Nagarik news',
            'summary': summary,
            'news_link': link,
            'image_link': None
        }
        main_news_list.append(news_dict)

    nep_date = main_news_list[0]['nep_date']
    cover_news_list = cover_news(nep_date)
    final_list = cover_news_list + main_news_list
    return final_list


if __name__ == '__main__':
    nagarik_international_extractor()
