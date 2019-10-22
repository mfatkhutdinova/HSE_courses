from flask_wtf import Form, validators
from wtforms import StringField
from wtforms import validators

class LoginForm(Form):
    id = StringField('id:', validators=[validators.required()])