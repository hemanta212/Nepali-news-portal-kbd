from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message
from flask_final import app, bcrypt, db, mail
from flask_final.forms import(SignupForm, LoginForm, RequestResetForm,
                              PasswordResetForm)
from flask_final.models import User
from flask_final.models import NepNationalNews as NNN
from flask_final.models import NepInternationalNews as NIN
from flask_final.models import EngNationalNews as ENN

from flask_final.utils import news_fetcher


@app.route("/", methods=["GET", 'POST'])
@app.route("/home", methods=["GET", 'POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('news'))
    return render_template('home.html',)


@app.route("/about", methods=["GET", 'POST'])
def about():
    return render_template('about.html', title="About US")


@app.route("/signup", methods=["GET", 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('news'))
    form = SignupForm()
    if form.validate_on_submit():

        flash('Your account is created', 'success')
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        user = User(full_name=form.full_name.data, email=form.email.data,
                    password=hashed_password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', title="Sign Up", form=form)


@app.route("/login", methods=["GET", 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('news'))
        else:
            flash('Invalid email or password. Try again!', "info    ")
            return redirect(url_for('login'))
    return render_template('login.html', title="Sign Up", form=form)


@login_required
@app.route("/logout", methods=["GET", 'POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_required
@app.route("/dashboard/news", methods=["GET", 'POST'])
def news():
    """Combo of all news models.

    Takes sample news from all models

     Ouput:
         many list of models items."""
    news_fetcher(NNN)
    news_fetcher(NIN)  # Reload all the models to get the latest news!!
    news_fetcher(ENN)

    NNN_list = NNN.query.order_by(NNN.date.desc())[:5]
    ENN_list = ENN.query.order_by(ENN.date.desc())[:5]
    NIN_list = NIN.query.order_by(NIN.date.desc())[:5]

    return render_template("news.html", ENN_list=ENN_list, NIN_list=NIN_list, NNN_list=NNN_list)


@login_required
@app.route("/dashboard/news/nep/national", methods=["GET", 'POST'])
def nep_national_news():
    """Save extracted news to model & passes to template"""
    news_fetcher(NNN)
    page = request.args.get("page", 1, type=int)
    news_list = NNN.query.order_by(NNN.date.desc()).paginate(page=page,
                                                             per_page=10)
    return render_template("nep_national_news.html", news_list=news_list)


@login_required
@app.route("/dashboard/news/nep/international", methods=["GET", 'POST'])
def nep_international_news():
    """Save extracted news to model & passes to template"""
    news_fetcher(NIN)
    page = request.args.get("page", 1, type=int)
    news_list = NIN.query.order_by(NIN.date.desc()).paginate(page=page,
                                                             per_page=10)
    return render_template("nep_international_news.html", news_list=news_list)


@login_required
@app.route("/dashboard/news/eng/national", methods=["GET", 'POST'])
def eng_national_news():
    """Save extracted news to model & passes to template"""
    news_fetcher(ENN)
    page = request.args.get("page", 1, type=int)
    news_list = ENN.query.order_by(ENN.date.desc()).paginate(page=page,
                                                             per_page=10)
    return render_template("eng_national_news.html", news_list=news_list)


@app.route("/password/reset", methods=["GET", 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_mail(user)
        flash('Email with reset link is sent. Check your email!')
        return redirect(url_for('login'))
    return render_template("reset_request.html", titile="Reset password",
                           form=form)


@app.route("/password/reset/<token>", methods=["GET", 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        flash('Logout and change your password.', 'info')
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

    return render_template('reset_password.html', form=form)


def send_reset_mail(user):
    token = user.get_reset_token()
    msg = Message('Reset Password for Khabar Board',
                  sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''{user.full_name}, you can have your password reset in below
    link {url_for('reset_token', token=token, _external =True)} if
    you have not sent this email then you can just ignore it'''

    mail.send(msg)
