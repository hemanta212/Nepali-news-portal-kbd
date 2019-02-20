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


def kathmandu_post_extractor():
    def featured():
        featured_news = []
        sticky_news = soup.find_all('div', class_="sticky-news")

        for news in sticky_news:
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
                    date = news.find('div', class_="post").text.split(",")[\
                        1].rstrip().lstrip()
                except IndexError:
                    date = 'error'
            print(date)
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

            featured_news.append(news_dict)
        return featured_news

    def main_news():
        main_news = soup.find('div', class_="main-news")
        news_list = main_news.find_all('div', class_="item")
        main_list = []

        for news in news_list:
            post_link = news.h2.a['href']
            default_link = "https://kathmandupost.ekantipur.com"
            full_link = default_link + post_link
            title = news.h2.a.text
            image_div = news.find('div', class_='ktp-main-news')
            if image_div is None:
                continue
            else:
                try:
                    image_link = image_div.img['data-original']
                except:
                    image_link = "img not available"

            # dealing with variable date location during parsing.
            try:
                date = news.find('div', class_="post").text.split(", ")[
                    2].rstrip()
            except IndexError:
                date = news.find('div', class_="post").text.split(", ")[
                    1].rstrip()

            summary = news.find('div', class_="text").text
            news_dict = {
                "image_link": image_link,
                "title": title,
                "nep_date": date,
                "source": "ekantipur",
                "news_link": full_link,
                "summary": summary,
            }
            main_list.append(news_dict)
            last_list = featured() + main_list

        return last_list

    return main_news()


if __name__ == "__main__":
    kathmandu_post_extractor()
