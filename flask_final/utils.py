from flask_final.nagarik_international import nagarik_international_extractor
from flask_final.kantipur_daily import kantipur_daily_extractor
from flask_final.kathmandupost import kathmandu_post_extractor
from flask_final.models import NepNationalNews as NNN
from flask_final.models import NepInternationalNews as NIN
from flask_final.models import EngNationalNews as ENN
from flask_final import db


def news_fetcher(category):
    category_dict = {
        NNN: kantipur_daily_extractor(),
        NIN: nagarik_international_extractor(),
        ENN: kathmandu_post_extractor(),
    }
    print("I am runing after declaration of dict")
    raw_news_list = category_dict[category]
    print("I am runing after declaration of raw_news_list")
    try:
        for news in raw_news_list[::-1]:
            dup = category.query.filter_by(title=news["title"]).first()

            if dup == None:
                news_post = category(title=news['title'],
                                     source=news['source'], summary=news['summary'],
                                     image_link=news['image_link'], news_link=news['news_link'],
                                     nep_date=news["nep_date"])

                db.session.add(news_post)
                db.session.commit()

        for i in category.query.order_by(category.date.asc())[30:]:
            db.session.delete(i)
            db.session.commit()
    except:
        pass
