from app.models.user import User

__author__ = 'erik'
from flask_wtf import Form, RecaptchaField
from wtforms.fields import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from pycountry import countries

COUNTRIES = [country.alpha2 for country in countries.objects]


def create_countries_dict():
    country_dict = []
    for _country in COUNTRIES:
        country_dict.append((_country, countries.get(alpha2=_country).name))
    return country_dict


class SignUpForm(Form):
    login = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match'),
                                                     Length(min=7, max=80)])
    confirm = PasswordField('Confirm')
    country = SelectField(choices=create_countries_dict())
    recaptcha = RecaptchaField()

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)

        user_by_username = User.query.filter_by(username=self.login.data).first()
        user_by_email = User.query.filter_by(email=self.email.data).first()

        if user_by_username is not None:
            self.login.errors.append('This username has already taken')
            return False

        if user_by_email is not None:
            self.email.errors.append('This email is using for another account')
            return False

        if not rv:
            return False

        self.user = user_by_username
        return True



