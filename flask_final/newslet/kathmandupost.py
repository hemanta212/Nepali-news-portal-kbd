'''
Script to scrape news from kathmandupost.ekantipur.com
Contains:
    kathmandu_post_extractor(): Gives list of news dicts
 '''

from bs4 import BeautifulSoup as BS
import requests

count = 0
url = 'https://kathmandupost.ekantipur.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

try:
    page = requests.get(url, headers=headers)
except Exception as e:
    print("Connection refused by the server..", e)

soup = BS(page.content, 'lxml')


def featured():
    '''
    This is a helper func to kathmandu_post_extractor func.
    It is mixed with kantipur_daily_extractor so you dont have
    to call it.

    This extracts top (latest) 1/2 featured news having diffrent set
    of layouts thant main news section

    Retruns:
        Same layout  that of kantipur_daily_extractor func

    '''
    featured_news_list = []
    sticky_news_list = soup.find_all('div', class_="sticky-news")

    for news in sticky_news_list:
        img_div = news.find('div', class_='image')
        try:
            img_link = img_div.img['data-original']
        except:
            img_link = "img not available"

        default_link = "https://kathmandupost.ekantipur.com"
        post_link = news.h1.a['href']
        full_link = default_link + post_link
        title = news.h1.a.text

        try:
            date = news.find('div', class_="post").text.split(",")[
                2].rstrip().lstrip()
        except IndexError:
            try:
                date = news.find('div', class_="post").text.split(",")[
                    1].rstrip().lstrip()
            except IndexError:
                date = 'error'
        summary = news.find('div', class_="text").text
        if len(summary) >= 1001:
            summary = summary[:1000]

        news_dict = {
            "title": title,
            "source": "ekantipur",
            "news_link": full_link,
            'nep_date': date,
            "summary": summary,
            "image_link": img_link,
        }

        featured_news_list.append(news_dict)

    return featured_news_list


def kathmandu_post_extractor():
    '''Extracts the news from https://kathmandupost.ekantipur.com
       with the same order as that of the website
    Retruns:
        A list containing dictionaries of news list[0] has latest
        example of such dictionary is
        {
                "image_link": image_link,
                "title": title in englist,
                "nep_date": date in 23 Mar 2018 format,
                "source": "ekantipur",
                "news_link": full_link,
                "summary": summary,
        }

    '''
    # the main news system is divided in 3 divs with
    # diffrent main classes  but inside layout is same
    main_news_div1 = soup.find('div', class_="main-news")
    main_news_div2 = soup.find('div', class_="news")
    main_news_div3_pre = soup.find('div', class_="home-featured-news")
    main_news_div3 = main_news_div3_pre.find('div', class_='newslist')

    sources = [main_news_div1, main_news_div2, main_news_div3]
    main_news_list = []

    for i in sources:
        news_list = i.find_all('div', class_="item")
        for news in news_list:
            post_link = news.h2.a['href']
            default_link = "https://kathmandupost.ekantipur.com"
            full_link = default_link + post_link
            title = news.h2.a.text
            image_div = news.find('div', class_='ktp-main-news')

            try:
                image_link = image_div.img['data-original']
            except AttributeError:
                image_link = None

            # dealing with variable date location during parsing.
            try:
                date = news.find('div', class_="post").text.split(",")[
                    2].rstrip()
            except IndexError:
                try:
                    date = news.find('div', class_="post").text.split(",")[
                        1].rstrip()
                except IndexError:
                    date = "error"

            summary = news.find('div', class_="text").text
            news_dict = {
                "image_link": image_link,
                "title": title,
                "nep_date": date,
                "source": "ekantipur",
                "news_link": full_link,
                "summary": summary,
            }
            main_news_list.append(news_dict)

    # mix latest news from featured helper funtion
    all_news_list = featured() + main_news_list
    return all_news_list


if __name__ == "__main__":
    kathmandu_post_extractor()
