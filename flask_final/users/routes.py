"""
contains resource for managing users functionality.
"""
from flask import Blueprint
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message
from flask_final import bcrypt, db, mail
from flask_final.users.forms import(SignupForm, LoginForm, RequestResetForm,
                                    PasswordResetForm)
from flask_final.users.models import User
users = Blueprint('users', __name__)


@users.route("/signup", methods=["GET", 'POST'])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for('newslet.news'))
    form = SignupForm()
    if form.validate_on_submit():

        flash('Your account is created', 'success')
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        user = User(full_name=form.full_name.data, email=form.email.data,
                    password=hashed_password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('signup.html', title="Sign Up", form=form)


@users.route("/try", methods=["GET", 'POST'])
def tryfree():
    if current_user.is_authenticated:
        return redirect(url_for('newslet.news'))
    user = User.query.filter_by(email="try@try.com").first()
    if not user:
        hashed_password = bcrypt.generate_password_hash('try').decode('utf-8')
        user = User(full_name="try", email="try@try.com",
                    password=hashed_password)

        db.session.add(user)
        db.session.commit()
    login_user(user, remember=True)
    return redirect(url_for('newslet.news'))


@users.route("/login", methods=["GET", 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('newslet.news'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('newslet.news'))
        else:
            flash('Invalid email or password. Try again!', "info    ")
            return redirect(url_for('users.login'))
    return render_template('login.html', title="Log in", form=form)


@users.route("/logout", methods=["GET", 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/password/reset", methods=["GET", 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_mail(user)
        flash('Email with reset link is sent. Check your email!')
        return redirect(url_for('users.login'))
    return render_template("reset_request.html", titile="Reset password",
                           form=form)


@users.route("/password/reset/<token>", methods=["GET", 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        flash('Logout and change your password.', 'info')
        return redirect(url_for('newslet.news'))

    user = User.verify_reset_token(token)
    if user is None:
        flash('Invalid or expired token!', 'warning')
        return redirect(url_for('users.reset_request'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        flash("Your password has been succesfully updated! Login now. ",
              'success')
        hashed_password = bcrypt.generate_password_hash(form.password.data).\
            decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('reset_password.html', title='Password reset',
                           form=form)


def send_reset_mail(user):
    token = user.get_reset_token()
    msg = Message('Reset Password for Khabar Board',
                  sender='noreply@demo.com', recipients=[user.email])
    msg.html = render_template('reset_password_email.html', action_url=url_for
                               ('users.reset_token', token=token, _external=True), user=user)
    # msg.body = f'''{user.full_name}, you can have your password reset in below
    # link {url_for('reset_token', token=token, _external =True)} if
    # you have not sent this email then you can just ignore it'''

    mail.send(msg)
