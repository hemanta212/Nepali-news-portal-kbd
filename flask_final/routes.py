from flask import render_template, url_for, redirect, flash,request
from flask_login import login_user, logout_user, current_user,login_required
from flask_mail import Message
from flask_final import app, bcrypt, db, mail
from flask_final.forms import SignupForm, LoginForm, RequestResetForm,
PasswordResetForm
from flask_final.models import User
from flask_final.models import NepNationalNews as NNN
from flask_final.models import NepInternationalNews as NIN
from flask_final.models import EngNationalNews as ENN

from flask_final.nagarik_international import nagarik_international_extractor
from flask_final.kantipur_daily import kantipur_daily_extractor
from flask_final.kathmandupost import kathmandu_post_extractor


@app.route("/",methods=["GET",'POST'])
@app.route("/home",methods=["GET",'POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('news'))
    return render_template('home.html',)

@app.route("/about",methods=["GET",'POST'])
def about():
    return render_template('about.html', title ="About US")

@app.route("/signup",methods=["GET",'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('news'))
    form = SignupForm()
    if form.validate_on_submit():

        flash('Your account is created','success')
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        user = User(full_name=form.full_name.data, email = form.email.data,
                    password = hashed_password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', title ="Sign Up", form = form )

@app.route("/login",methods=["GET",'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            flash('You are logged in','success')
            login_user(user, remember = form.remember.data)
            return redirect(url_for('news'))
        else:
            flash('Invalid username or password. Try again!', "info    ")
            return redirect(url_for('login'))
    return render_template('login.html', title ="Sign Up", form = form )



@login_required
@app.route("/logout",methods=["GET",'POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
@app.route("/dashboard/news",methods=["GET",'POST'])
def news():
    """Combo of all news models.

    Takes sample news from all models

     Ouput:
         many list of models items."""
    NNN_list = NNN.query.order_by(NNN.date)[:5]
    ENN_list = ENN.query.order_by(ENN.date)[:5]
    NIN_list = NIN.query.order_by(NIN.date)[:5]
    return render_template("news.html", ENN_list = ENN_list, NIN_list=NIN_list)

@login_required
@app.route("/dashboard/news/nep/national",methods=["GET",'POST'])
def nep_national_news():
    """Save extracted news to model & passes to template"""
    kantipur_daily_news_list = kantipur_daily_extractor()
    for news in kantipur_daily_news_list[::-1]:
        dup =  NNN.query.filter_by(summary = news["summary"]).first()
        if dup == None:
            news_post = NNN(title  = news['title'], nep_date  = news['date'],
                            source  = news['source'],summary = news['summary'],
                            news_link = news['news_link'],)
            db.session.add(news_post)
            db.session.commit()
    try:
        for i in NNN.query.order_by(NNN.date)[10:]:
            db.session.delete(i)
            db.session.commit()
    finally:
        page = request.args.get("page",1,type=int)
        news_list = NNN.query.order_by(NNN.date.desc()).paginate(page=page,
                                                                 per_page=10)

    return render_template("nep_national_news.html", news_list = news_list)

@login_required
@app.route("/dashboard/news/nep/international",methods=["GET",'POST'])
def nep_international_news():
    """Save extracted news to model & passes to template"""
    nagarik_international_news_list = nagarik_international_extractor()

    for news in nagarik_international_news_list[::-1]:
        dup =  NIN.query.filter_by(summary = news["summary"]).first()
        if dup == None:
            news_post =NIN(title  = news['title'], nep_date  = news['date'],
                           source  = news['source'], summary = news['summary'],
                           news_link = news['news_link'])
            db.session.add(news_post)
            db.session.commit()
    try:
        for i in NIN.query.order_by(NIN.date)[10:]:
            db.session.delete(i)
            db.session.commit()
    finally:
        page = request.args.get("page",1,type=int)
        news_list = NIN.query.order_by(NIN.date.desc()).paginate(page=page,
                                                                 per_page=10)

    return render_template("nep_international_news.html", news_list= news_list)

@login_required
@app.route("/dashboard/news/eng/national",methods=["GET",'POST'])
def eng_national_news():
    """Save extracted news to model & passes to template"""
    kathmandu_post_news_list = kathmandu_post_extractor()
    for news in kathmandu_post_news_list[::-1]:
        dup =  ENN.query.filter_by(summary = news["summary"]).first()
        if dup == None:
            news_post = ENN(title  = news['title'], nep_date  = news['date'],
                            source  = news['source'],
                            summary = news['summary'],
                            news_link = news['news_link'],
                            image_link=news['image_link'])
            db.session.add(news_post)
            db.session.commit()

    try:
        for i in ENN.query.order_by(ENN.date)[10:]:
            db.session.delete(i)
            db.session.commit()
    finally:
        page = request.args.get("page",1,type=int)
        news_list = ENN.query.order_by(ENN.date.desc()).paginate(page=page,
                                                                 per_page=10)

    return render_template("eng_national_news.html", news_list = news_list)


@app.route("/password/reset",methods=["GET",'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_mail(user)
        flash('Email with reset link is sent. Check your email!')
        return redirect(url_for('login'))
    return render_template("reset_request.html", titile ="Reset password",
                           form= form)

@app.route("/password/reset/<token>",methods=["GET",'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        flash('Logout and change your password.','info')
        return redirect(url_for('news'))

    user = User.verify_reset_token(token)
    if user is None:
        flash('Invalid or expired token!', 'warning')
        return redirect(url_for('reset_request'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        flash("Your password has been succesfully updated! Login now. ",
              'success')
        hashed_password = bcrypt.generate_password_hash(form.password.data).\
        decode('utf-8')
        user.password = hashed_password
        db.session.commit()
    return redirect(url_for('login'))

    return render_template('password_reset.html', form = form    )

def send_reset_mail(user):
    token = user.get_reset_token()
    msg = Message('Reset Password for Khabar Board',
                  sender = 'noreply@demo.com', recipients= [user.email])
    msg.body = f'''{user.full_name}, you can have your password reset in below
    link {url_for('reset_token', token=token, _external =True)} if
    you have not sent this email then you can just ignore it'''

    mail.send(msg)
