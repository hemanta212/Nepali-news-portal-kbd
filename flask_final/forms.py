from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_final.models import User


class SignupForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired(), Length(max=20, min=3)])
    email = StringField("Email-address", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=3)])
    confirm_password = PasswordField("confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign UP')

    def validate_email(self, email):
        duplicate_user = User.query.filter_by(email=email.data).first()
        if duplicate_user:
            flash('Email already registered. try another', 'success')
            raise ValidationError('Email already registered. try another')


class LoginForm(FlaskForm):
    email = StringField("Email-address", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=3)])
    remember = BooleanField("Remember me")
    submit = SubmitField('Log in')

   # def verify_login(self,password):


class RequestResetForm(FlaskForm):
    email = StringField("Email-address", validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        registered_user = User.query.filter_by(email=email.data).first()
        if registered_user == None:
            flash('Email not registered. try another', 'warning')
            raise ValidationError('Email not registered. try another')


class PasswordResetForm(FlaskForm):
    password = PasswordField("password", validators=[DataRequired(), Length(min=3)])
    confirm_password = PasswordField("confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset')
