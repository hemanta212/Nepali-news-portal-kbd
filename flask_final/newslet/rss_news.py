import html
import feedparser
from bs4 import BeautifulSoup


def get_news_from_rss(source, feed_url=None):
    url_map = {
        "himalayan_times": "http://thehimalayantimes.com/feed/",
        "ujyaalo_online": "http://ujyaaloonline.com/rss/",
    }

    feed_url = feed_url if feed_url else url_map[source]
    news_list = parse_feed_for_news(feed_url)
    add_source_to_news(news_list, source)
    return news_list


def parse_feed_for_news(feed_url):
    feed = feedparser.parse(feed_url)
    entries = feed.entries
    news = get_news_from_entries(entries)
    return news


def add_source_to_news(news_list, source):
    for news_dict in news_list:
        news_dict["source"] = source


def get_news_from_entries(entries):
    news_list = []
    for entry in entries:
        title = entry.get("title")
        if not title:  # There must be title else skip
            continue

        summary = entry.get("summary")
        if summary:
            summary = parse_text_from_html(summary)
            summary = escape_html_charectars(summary)

        date = entry.get("published")
        if date:  # Wed, 13 Oct 2019 10:56:09 +00000'
            date = date.split(" ")
            date = " ".join([date[1], date[2], date[3]])

        link = entry.get("link")
        entry_dict = {
            "title": title,
            "raw_date": date,
            "image_link": "",
            "summary": summary,
            "news_link": link,
        }
        news_list.append(entry_dict)
    return news_list


def escape_html_charectars(text):
    chars = ["&amp;nbsp;", "&amp;", "&amp;ndash;", "&ndash;"]
    for char in chars:
        text = text.replace(char, html.unescape(char))
    return text


def parse_text_from_html(html):
    tree = BeautifulSoup(html, "lxml")

    body = tree.body
    if body is None:
        return None

    for tag in body.select("script"):
        tag.decompose()
    for tag in body.select("style"):
        tag.decompose()

    text = body.get_text(separator="\n")
    return text
