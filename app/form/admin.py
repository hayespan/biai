# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, StringField, BooleanField, DateField, IntegerField, PasswordField, DecimalField
from wtforms.validators import Required, Length, Optional, ValidationError, Regexp
from ..util.regexp import mobile_s, captcha_s


class LoginForm(Form):
    username = StringField(validators=[Required(), Length(1, 64), ])
    password = PasswordField(validators=[Required(), ])
    remember_me = BooleanField()
