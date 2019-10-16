"""
Script to scrape news from www.kantipurdaily.com/world
Contains:
    kantipur_international_extractor(): Gives list of news dicts
"""
from datetime import datetime
from bs4 import BeautifulSoup as BS
import requests

try:
    from flask_final.newslet import parser
except ImportError:
    parser = "lxml"


def setup():
    url = "https://www.kantipurdaily.com/world"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    try:
        page = requests.get(url, headers=headers)
    except Exception as e:
        print("Connection refused by the server..", e)

    soup = BS(page.content, parser)
    return soup


def kantipur_international_extractor():
    """
    Scrapes news from www.kantipurdaily.com/world
    Retruns:
        A list containing dictionaries of news. list[0] has latest
        The format or attributes of dictionary is like this sample
        {
            'title': title in nepali,
            'raw_date': date in 2019/02/34 format,
            'source': 'ekantipur',
            'summary': summary in nepali,
            'news_link': link,
            'image_link': high resolution image,
        }
    """
    soup = setup()
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
        date = format_date(date)
        link = "https://kantipurdaily.com" + date_ore

        news_dict = {
            "title": title,
            "raw_date": date,
            "source": "ekantipur",
            "summary": summary,
            "news_link": link,
            "image_link": big_img,
        }
        news_list.append(news_dict)

    return news_list


def format_date(raw_date):
    org_format = "%Y/%m/%d"
    datetime_obj = datetime.strptime(raw_date, org_format)
    dest_format = "%d %b %Y"
    date = datetime_obj.strftime(dest_format)
    return date


if __name__ == "__main__":
    kantipur_international_extractor()
