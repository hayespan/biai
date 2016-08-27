# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, StringField, BooleanField, DateField, IntegerField, PasswordField, DecimalField
from wtforms.validators import Required, Length, Optional, ValidationError, Regexp
from ..util.regexp import captcha_s, mobile_s

class CooperationForm(Form):
    name = StringField(validators=[Required(), ])
    contact = StringField(validators=[Required(), ])
    zone = StringField(validators=[Required(), Length(1, 512), ])
    shop_range = StringField(validators=[Required(), Length(1, 1024), ])
    develop_plan = TextAreaField(validators=[Required(), ])
    cooperation_intention = TextAreaField(validators=[Required(), ])
    mobile = StringField(validators=[Required(), Regexp(mobile_s)])
    code = StringField(validators=[Required(), Regexp(captcha_s), ])

