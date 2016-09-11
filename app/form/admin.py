# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, StringField, BooleanField, DateField, IntegerField, PasswordField, DecimalField
from wtforms.validators import Required, Length, Optional, ValidationError, Regexp
from ..util.regexp import mobile_s, captcha_s

class UploadProductPicForm(Form):
    pic = FileField(validators=[FileRequired(), ])

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

class CUProductCategoryForm(Form):
    id = IntegerField()
    name = StringField(validators=[Length(0, 512), ])
    img = FileField()
    weight = IntegerField()

class RDProductCategoryForm(Form):
    id = IntegerField(validators=[Required(), ])

class CUProductForm(Form):
    id = IntegerField()
    name = StringField(validators=[Length(0, 512), ])
    attrs = StringField()
    oth_attrs = StringField()
    buy_link = StringField()
    description = StringField()
    category_ids = StringField()
    file_ids = StringField()

class RDProductForm(Form):
    id = IntegerField(validators=[Required(), ])

class RDCreativityForm(Form):
    id = IntegerField(validators=[Required(), ])

class USimpleNavPageForm(Form):
    id = IntegerField(validators=[Required(), ])
    content = TextAreaField()

class CBannerForm(Form):
    weight = IntegerField(validators=[])
    name = StringField(validators=[Required(), Length(0, 512), ])
    pic = FileField(validators=[FileRequired(), ])

class DBannerForm(Form):
    id = IntegerField(validators=[Required(), ])

class CVideoForm(Form):
    weight = IntegerField(validators=[])
    name = StringField(validators=[Required(), Length(0, 512), ])
    pic = FileField(validators=[FileRequired(), ])
    video = FileField(validators=[FileRequired(), ])

class DVideoForm(Form):
    id = IntegerField(validators=[Required(), ])

class CInformationForm(Form):
    title = StringField(validators=[Required(), ])
    weight = IntegerField()
    news_id = IntegerField(validators=[Required(), ])

class DInformationForm(Form):
    id = IntegerField(validators=[Required(), ])

class DCooperationForm(Form):
    id = IntegerField(validators=[Required(), ])

class UNavForm(Form):
    id = IntegerField(validators=[Required(), ])
    title = StringField(validators=[Required(), ])
    link = StringField(validators=[Required(), ])
