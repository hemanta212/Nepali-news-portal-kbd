from bs4 import BeautifulSoup as BS
import requests


url = 'https://www.kantipurdaily.com/world'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


try:
    page = requests.get(url, headers=headers)
except Exception as e:
    print("Connection refused by the server..", e)

soup = BS(page.content, 'lxml')


def kantipur_international_extractor():
   # with codecs.open("kantipur_daily_cache.csv", "w", encoding='utf-8', errors='ignore') as w:
        # with open("kantipur_daily_cache.csv", 'w') as w:

    counter = 0
    news_list = []
    for article in soup.find_all('article', class_='normal'):

        title = article.h2.a.text
        #author = article.find('div', class_='author').text
        summary = article.find('p').text
        image = article.find('div', class_="image").figure.a.img["data-src"]
        img = image.replace("-lowquality", "")
        small_img = img.replace("lowquality", "")
        big_img = small_img.replace("300x0", "1000x0")
        date_ore = article.h2.a['href']
        contaminated_list = date_ore.split('/')
        pure_date_list = [contaminated_list[2],
                          contaminated_list[3], contaminated_list[4]]
        date = "/".join(pure_date_list)
        link = "https://kantipurdaily.com" + date_ore
        news_dict = {
            'title': title,
            'nep_date': date,
            'source': 'ekantipur',
            'summary': summary,
            'news_link': link,
            'image_link': big_img,
        }
        news_list.append(news_dict)
        counter += 1
    return news_list


if __name__ == "__main__":
    kantipur_international_extractor()
