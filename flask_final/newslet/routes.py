"""Author : Hemanta Sharma
Contains routes for managing news.
"""
from flask import Blueprint
from flask import request, render_template
from flask_login import login_required
from flask_final.newslet.models import NepNationalNews as NNN
from flask_final.newslet.models import NepInternationalNews as NIN
from flask_final.newslet.models import EngNationalNews as ENN
from flask_final.newslet.utils import news_fetcher

newslet = Blueprint('newslet', __name__)


@newslet.route("/dashboard/news", methods=["GET", 'POST'])
@login_required
def news():
    """Combo of all news models.

    Takes sample news from all models

    Ouput:
       many list of models items."""
    news_fetcher('NNN')
    news_fetcher('NIN')  # Reload all the models to get the latest news!!
    news_fetcher('ENN')

    NNN_list = NNN.query.order_by(NNN.date.desc())[:5]
    ENN_list = ENN.query.order_by(ENN.date.desc())[:5]
    NIN_list = NIN.query.order_by(NIN.date.desc())[:5]

    return render_template("news.html", ENN_list=ENN_list, NIN_list=NIN_list,
                           NNN_list=NNN_list)


@newslet.route("/dashboard/news/nep/national", methods=["GET", 'POST'])
@login_required
def nep_national_news():
    """Save extracted news to model & passes to template"""
    news_fetcher('NNN')
    page = request.args.get("page", 1, type=int)
    news_list = NNN.query.order_by(NNN.date.desc()).paginate(page=page,
                                                             per_page=10)
    return render_template("detail_news.html", title='National-Nep',
                           news_list=news_list,
                           heading='National News [नेपा]',
                           newslet_func='newslet.nep_national_news',
                           read_more='|थप पढ्नुहोस >>|')


@newslet.route("/dashboard/news/nep/international", methods=["GET", 'POST'])
@login_required
def nep_international_news():
    """Save extracted news to model & passes to template"""
    news_fetcher('NIN')
    page = request.args.get("page", 1, type=int)
    news_list = NIN.query.order_by(NIN.date.desc()).paginate(page=page,
                                                             per_page=10)
    return render_template("detail_news.html", title='International-Nep',
                           news_list=news_list,
                           heading='International News [नेपा]',
                           newslet_func='newslet.nep_international_news',
                           read_more='|थप पढ्नुहोस >>|')


@newslet.route("/dashboard/news/eng/national", methods=["GET", 'POST'])
@login_required
def eng_national_news():
    """Save extracted news to model & passes to template"""
    news_fetcher('ENN')
    page = request.args.get("page", 1, type=int)
    news_list = ENN.query.order_by(ENN.date.desc()).paginate(page=page,
                                                                 per_page=10)
    return render_template("detail_news.html", title='National-Eng',
                           news_list=news_list,
                           heading='National News [Eng]',
                           newslet_func='newslet.eng_national_news',
                           read_more='|Read More>>|')
