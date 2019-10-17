# -*-code; UTF_8
"""
Contains routes for managing news.
    news(): Mix collech 3 samples
    Detail news routes
        nep_national_news()
        nep_international_news()
        eng_national_news()
        eng_international_news()
"""

from flask import Blueprint
from flask import request, render_template
from flask_login import login_required, current_user
from flask_final.newslet.models import NepNationalNews as NNN
from flask_final.newslet.models import NepInternationalNews as NIN
from flask_final.newslet.models import EngNationalNews as ENN
from flask_final.newslet.models import EngInternationalNews as EIN
from flask_final.newslet.news_loader import load_news_to_models

newslet = Blueprint("newslet", __name__)


@newslet.route("/dashboard/news", methods=["GET"])
@newslet.route("/dashboard/news/nep/national", methods=["GET"])
def nep_national_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """

    load_news_to_models("NNN")
    page = request.args.get("page", 1, type=int)
    free_sources = ("ujyaalo_online",)
    news = NNN.query.filter_by(source=" ")
    logged = current_user.is_authenticated
    if not logged:
        for source in free_sources:
            news = news.union(NNN.query.filter_by(source=source)).order_by(
                NNN.date.desc()
            )

    else:
        news = NNN.query.order_by(NNN.date.desc())

    news_list = news.paginate(page=page, per_page=15)
    return render_template(
        "detail_news.html",
        title="National-Nep",
        news_list=news_list,
        heading="National News [नेपा]",
        newslet_func="newslet.nep_national_news",
        read_more="|थप पढ्नुहोस >>|",
        logged=logged,
    )


@newslet.route("/dashboard/news/nep/international", methods=["GET"])
@login_required
def nep_international_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """

    load_news_to_models("NIN")
    page = request.args.get("page", 1, type=int)
    news_list = NIN.query.order_by(NIN.date.desc()).paginate(page=page, per_page=15)
    return render_template(
        "detail_news.html",
        title="International-Nep",
        news_list=news_list,
        heading="International News [नेपा]",
        newslet_func="newslet.nep_international_news",
        read_more="|थप पढ्नुहोस >>|",
        logged=True,
    )


@newslet.route("/dashboard/news/eng/national", methods=["GET"])
def eng_national_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """
    load_news_to_models("ENN")
    page = request.args.get("page", 1, type=int)
    free_sources = ("himalayan_times",)
    news = ENN.query.filter_by(source=" ")
    logged = current_user.is_authenticated
    if not logged:
        for source in free_sources:
            news = news.union(ENN.query.filter_by(source=source)).order_by(
                ENN.date.desc()
            )
    else:
        news = ENN.query.order_by(ENN.date.desc())

    news_list = news.paginate(page=page, per_page=15)
    return render_template(
        "detail_news.html",
        title="National-Eng",
        news_list=news_list,
        heading="National News [Eng]",
        newslet_func="newslet.eng_national_news",
        read_more="|Read More>>|",
        logged=logged,
    )


@newslet.route("/dashboard/news/eng/international", methods=["GET"])
def eng_international_news():
    """
    Save extracted news from scraper to db model
    then passes to detail_news.html template to render it
    """
    load_news_to_models("EIN")
    load_news_to_models("NNN")
    load_news_to_models("ENN")
    page = request.args.get("page", 1, type=int)
    news_list = EIN.query.order_by(EIN.date.desc()).paginate(page=page, per_page=15)
    logged = current_user.is_authenticated
    return render_template(
        "detail_news.html",
        title="International-Eng",
        news_list=news_list,
        heading="International News [Eng]",
        newslet_func="newslet.eng_international_news",
        read_more="|Read More>>|",
        logged=logged,
    )


@newslet.route("/update", methods=["GET"])
def update():
    categories = ("EIN", "NIN", "ENN")
    for category in categories:
        try:
            load_news_to_models(category)
        except Exception as E:
            print(E)

    return "<h1>Updated all news sources</h1>"
