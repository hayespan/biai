# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, StringField, BooleanField, DateField, IntegerField, PasswordField, DecimalField
from wtforms.validators import Required, Length, Optional, ValidationError, Regexp
from ..util.regexp import captcha_s, mobile_s

class SearchForm(Form):
    key = StringField('key', validators=[Required(), ])

class CaptchaForm(Form):
    code = StringField(validators=[Required(), Regexp(captcha_s)])

class MobileForm(Form):
    mobile = StringField(validators=[Required(), Regexp(mobile_s)])

