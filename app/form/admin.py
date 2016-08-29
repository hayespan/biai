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

class CUNewsCategoryForm(Form):
    id = IntegerField(validators=[])
    name = StringField(validators=[Length(0, 512), ])
    img = FileField(validators=[])
    weight = IntegerField()

class RDNewsCategoryForm(Form):
    id = IntegerField(validators=[Required(), ])

class CUNewsForm(Form):
    id = IntegerField(validators=[])
    title = StringField(validators=[Length(0, 1024), ])
    content = StringField(validators=[])
    news_category_id = IntegerField(validators=[])

class RDNewsForm(Form):
    id = IntegerField(validators=[Required(), ])

