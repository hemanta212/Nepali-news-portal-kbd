# -*-Code UTF-8
"""
forms for user registering
contains 4 classes:
    SignupForm
    LoginForm
    RequestResetForm
    PasswordResetForm
"""

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_final.users.models import User


class SignupForm(FlaskForm):
    """
    Form for signing up the user
    Attributes:
        full_name [str]: full name of user
        email [str]: email of the user
        password [password]: secret password
        confirm_password [password]: confirmed password
        submit [submit]: submit field
    Methods:
        validate_email(): checks if email is already registered
    """

    full_name = StringField(
        "Full Name", validators=[DataRequired(), Length(max=20, min=3)]
    )
    email = StringField("Email-address", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=3)])
    confirm_password = PasswordField(
        "confirm password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign UP")

    def validate_email(self, email):
        """
        Checks if email is already registered and raises a
        ValidationError and flashes a warning if so
        """

        duplicate_user = User.query.filter_by(email=email.data).first()
        if duplicate_user:
            flash("Email already registered. try another", "warning")
            raise ValidationError("Email already registered. try another")


class LoginForm(FlaskForm):
    """
    Form for logging in the user
    Attributes:
        email [str]: email of the user
        password [password]: secret password
        remember [bool]: checkbox for whether to remember sessions
        submit [submit]: submit field
    """

    email = StringField("Email-address", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=3)])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in")


class RequestResetForm(FlaskForm):
    """
    Form for the user to request his passowrd reset
    Attributes:
        email [str]: email of the user
        submit [submit]: submit field
    Methods:
        validate_email(): checks if email is registered
    """

    email = StringField("Email-address", validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        """
        Checks for the given email in database
        raises ValidationError and flashes waring if not found
        """

        registered_user = User.query.filter_by(email=email.data).first()
        if registered_user is None:
            flash("Email not registered. try another", "warning")
            raise ValidationError("Email not registered. try another")


class PasswordResetForm(FlaskForm):
    """
    Form for reseting the user's password
    Attributes:
        password [password]: secret password
        confirm_password [password]: confirmed password
        submit [submit]: submit field
    """

    password = PasswordField("password", validators=[DataRequired(), Length(min=3)])
    confirm_password = PasswordField(
        "confirm password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Reset")
