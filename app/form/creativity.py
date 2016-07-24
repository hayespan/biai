# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, StringField, BooleanField, DateField, IntegerField, PasswordField, DecimalField
from wtforms.validators import Required, Length, Optional, ValidationError, Regexp
from ...util.regexp import mobile_s, captcha_s

class PostCreativity(Form):
    img = FileField(validators=[FileRequired(), ])
    mobile = StringField(validators=[Required(), Regexp(mobile_s), ])
    code = StringField(validators=[Required(), Regexp(captcha_s), ])
