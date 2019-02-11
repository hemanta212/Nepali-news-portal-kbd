try:
    from flask_final.newslet.nagarik_international import nagarik_international_extractor
    from flask_final.newslet.kantipur_daily import kantipur_daily_extractor
    from flask_final.newslet.kathmandupost import kathmandu_post_extractor

except Exception as E:
    print(E)

    def news_fetcher(category):
        pass

else:
    from flask_final.newslet.models import NepNationalNews as NNN
    from flask_final.newslet.models import NepInternationalNews as NIN
    from flask_final.newslet.models import EngNationalNews as ENN
    from flask_final import db

    def news_fetcher(category):
        model_maps = {
            'NNN': NNN,
            'NIN': NIN,
            'ENN': ENN
        }
        extractor_maps = {
            'NNN': kantipur_daily_extractor,
            'NIN': nagarik_international_extractor,
            'ENN': kathmandu_post_extractor,
        }
        raw_news_list = extractor_maps[category]()

        for news in raw_news_list[::-1]:
            dup = model_maps[category].query.filter_by(
                title=news["title"]).first()

            if dup is None:
                news_post = model_maps[category](title=news['title'],
                                                 source=news['source'], summary=news['summary'],
                                                 image_link=news['image_link'], news_link=news['news_link'],
                                                 nep_date=news["nep_date"])

                db.session.add(news_post)
                db.session.commit()

        for i in model_maps[category].query.order_by(model_maps[category].date.asc())[30:]:
            db.session.delete(i)
            db.session.commit()
