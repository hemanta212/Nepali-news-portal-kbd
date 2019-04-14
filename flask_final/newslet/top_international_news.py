import os
import sys
import requests
import datetime

API_KEY = os.getenv('NEWS_API_KEY')

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
    AppleWebKit/537.36(KHTML, like Gecko)\
    Chrome/39.0.2171.95 Safari/537.36'
    }

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
format = '%Y-%m-%d'
from_ = yesterday.strftime(format)
to = today.strftime(format)

sources = ['al-jazeera-english', 'bbc-news', 'associated-press','cnn',
             'the-new-york-times', 'the-times-of-india']

def get_general_headlines(api_key, **kwargs):
    '''
    Returns: A list of news dictionaries
    Params: api_key*
    Optional_params: language, pageSize, page, apiKey, sources,
                        q, category, country
    '''

    basic_url = ['https://newsapi.org/v2/top-headlines?']
    for param,value in kwargs.items():
        string = '{0}={1}&'.format(param, value)
        basic_url.append(string)

    api_str = 'apiKey={0}'.format(api_key)
    sources_str = 'sources=' + ",".join(sources) + '&'
    basic_url.append(sources_str)
    basic_url.append(api_str)
    url = "".join(basic_url)
    try:
        response = requests.get(url, headers=headers)
    except:
        print("No internet Exiting....")
        sys.exit(1)

    response_dict = response.json()
    total_news = response_dict.get('totalResults')
    status = response_dict.get('status', 'error')
    news_list = response_dict['articles']
    refined_news_list = []
    for index, news in enumerate(news_list):
        title = news.get('title', 'error')
        try:
            source = news['source']['name']
        except:
            source = 'English press'

        news_url = news.get('url', 'error')
        image_url = news.get('urlToImage', 'error')
        summary = news.get('description', 'Read full news at..')
        pub_date = news.get('publishedAt', 'error')

        # '2019-03-04T08:45:39.4..Z' -> '2019-03-04 08:45:39.45..'
        raw_date = pub_date[:10] + ' ' + pub_date[12:-1]
        date = None
        try:
            raw_date, date = format_date(raw_date)
        except Exception as e:
            print(e)
            pass

        final_news_dict = {
            'title': title,
            'raw_date': raw_date,
            'date': date,
            'source': source,
            'summary':summary,
            'news_link': news_url,
            'image_link': image_url
        }
        refined_news_list.append(final_news_dict)

    return refined_news_list

def format_date(raw_date):
    org_format = '%Y-%m-%d %H:%M:%S'
    datetime_obj = datetime.datetime.strptime(raw_date, org_format)
    dest_format = '%d %b %Y'
    date_str = datetime_obj.strftime(dest_format)
    return date_str, datetime_obj


if __name__ == '__main__':
    get_general_headlines(API_KEY)
