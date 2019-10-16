"""
Script to scrape news from www.kantipurdaily.com/news
Contains:
    kantipur_daily_extractor(): Gives list of news dicts
 """
from bs4 import BeautifulSoup as BS
import requests
from datetime import datetime

try:
    from flask_final.newslet import parser
except ImportError:
    parser = "lxml"


def setup():
    url = "https://www.kantipurdaily.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit\
        /537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }
    try:
        page = requests.get(url, headers=headers)
    except Exception as e:
        print("Connection refused by the server..", e)
    soup = BS(page.content, parser)
    return soup


def kantipur_daily_extractor():
    """
    Extracts news from www.kantipurdaily.com/news
    Retruns
    The order is as given by the website
    A list containing news dictionaries. Here is a sample

        {
            title: str in nepali
            'raw_date': 2019/06/34 like date,
            'source': 'ekantipur',
            'summary': news summary in nepali,
            'news_link': link,
            'image_link': imglink,
        }

    """
    soup = setup()
    counter = 0
    news_list = []
    for article in soup.find_all("article", class_="normal"):

        title = article.h2.a.text
        summary = article.find("p").text
        image = article.find("div", class_="image").figure.a.img["data-src"]
        img = image.replace("-lowquality", "")
        small_img = img.replace("lowquality", "")
        big_img = small_img.replace("300x0", "1000x0")
        date_ore = article.h2.a["href"]
        contaminated_list = date_ore.split("/")
        pure_date_list = [
            contaminated_list[2],
            contaminated_list[3],
            contaminated_list[4],
        ]
        date = "/".join(pure_date_list)
        link = "https://kantipurdaily.com" + date_ore
        date = format_date(date)
        news_dict = {
            "title": title,
            "raw_date": date,
            "source": "ekantipur",
            "summary": summary,
            "news_link": link,
            "image_link": big_img,
        }
        news_list.append(news_dict)
        counter += 1

    return news_list


def format_date(raw_date):
    org_format = "%Y/%m/%d"
    datetime_obj = datetime.strptime(raw_date, org_format)
    dest_format = "%d %b %Y"
    date = datetime_obj.strftime(dest_format)
    return date


if __name__ == "__main__":
    kantipur_daily_extractor()
