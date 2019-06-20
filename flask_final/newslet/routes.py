# -*-code; UTF_8
"""
Contains routes for managing news.
    news(): Mix collech 3 samples
    Detail news routes
        nep_national_news()
        nep_international_news()
        eng_national_news()
"""

from flask import Blueprint
from flask import request, render_template
from flask_login import login_required
from flask_final.newslet.models import NepNationalNews as NNN
from flask_final.newslet.models import NepInternationalNews as NIN
from flask_final.newslet.models import EngNationalNews as ENN
from flask_final.newslet.models import EngInternationalNews as EIN
from flask_final.newslet.utils import news_fetcher

newslet = Blueprint('newslet', __name__)

nlakdjs = '''\
@newslet.route("/dashboard/news", methods=["GET"])
@login_required
def news():
    """
    Combo of all news models.
    Takes sample news from all models

    Returns:
       pass many list of models items to news.html template
       and rende  """

    categories = ('NIN', 'NNN', 'ENN', 'EIN')
    models = {}
    for category in categories:
        # Reload all the models to get the latest news!!
        news_fetcher(category)

        model = eval(category)  # change 'NNN' to NNN
        order = model.date.desc()  # order by latest date
        models[category + '_list'] = model.query.order_by(order)[:5]

    return render_template(
#        "news.html", title='Dashboard | Home', ENN_list=models['ENN_list'],
        NIN_list=models['NIN_list'], NNN_list=models['NNN_list'],
#        EIN_list=models['EIN_list'])

'''
@newslet.route("/dashboard/news", methods=["GET"])
@newslet.route("/dashboard/news/nep/national", methods=["GET"])
@login_required
def nep_national_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """

    news_fetcher('NNN')
    page = request.args.get("page", 1, type=int)
    news_list = NNN.query.order_by(NNN.date.desc()).paginate(page=page,
                                                             per_page=15)
    return render_template("detail_news.html", title='National-Nep',
                           news_list=news_list,
                           heading='National News [नेपा]',
                           newslet_func='newslet.nep_national_news',
                           read_more='|थप पढ्नुहोस >>|')


@newslet.route("/dashboard/news/nep/international", methods=["GET"])
@login_required
def nep_international_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """

    news_fetcher('NIN')
    page = request.args.get("page", 1, type=int)
    news_list = NIN.query.order_by(NIN.date.desc()).paginate(page=page,
                                                             per_page=15)
    return render_template("detail_news.html", title='International-Nep',
                           news_list=news_list,
                           heading='International News [नेपा]',
                           newslet_func='newslet.nep_international_news',
                           read_more='|थप पढ्नुहोस >>|')


@newslet.route("/dashboard/news/eng/national", methods=["GET"])
@login_required
def eng_national_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """
    news_fetcher('ENN')
    page = request.args.get("page", 1, type=int)
    news_list = ENN.query.order_by(ENN.date.desc()).paginate(page=page,
                                                             per_page=15)
    return render_template("detail_news.html", title='National-Eng',
                           news_list=news_list,
                           heading='National News [Eng]',
                           newslet_func='newslet.eng_national_news',
                           read_more='|Read More>>|')


@newslet.route("/dashboard/news/eng/international", methods=["GET"])
@login_required
def eng_international_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """
    news_fetcher('EIN')
    page = request.args.get("page", 1, type=int)
    news_list = EIN.query.order_by(EIN.date.desc()).paginate(page=page,
                                                             per_page=15)
    return render_template("detail_news.html", title='International-Eng',
                           news_list=news_list,
                           heading='International News [Eng]',
                           newslet_func='newslet.eng_international_news',
                           read_more='|Read More>>|')
