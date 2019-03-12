from bs4 import BeautifulSoup as BS
import requests
import codecs

try:
    from flask_final import Kbdlog
    logger = Kbdlog(file='kbd.log', debug_file='/newslet/kantipur.log', console=False).get_logger()

except ModuleNotFoundError:
    print("Running in single mode no loggers attached")

url = 'https://www.kantipurdaily.com/news'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



try:
    page = requests.get(url, headers=headers)
except Exception as e:
    print("Connection refused by the server..", e)
soup = BS(page.content, 'lxml')

def custom_nepali_logger(msg, data):
    debug_file = 'flask_final/logs/newslet/kantipur.log'
#    debug_file = '../logs/newslet/kantipur.log'
    with codecs.open(debug_file, "a", encoding='UTF-8', errors='ignore') as w:
        w.writelines(msg)
        w.writelines(data)

def kantipur_daily_extractor():

    counter = 0
    news_list = []
    for article in soup.find_all('article', class_='normal'):

        title = article.h2.a.text
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
    custom_nepali_logger('titles:', [i['nep_date'] for i in news_list])
    return news_list


if __name__ == "__main__":
    kantipur_daily_extractor()

