# -*- coding: utf-8 -*-
from ..util.common import logger
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField, StringField, BooleanField, DateField, IntegerField, PasswordField, DecimalField
from wtforms.validators import Required, Length, Optional, ValidationError, Regexp
from ..util.regexp import mobile_s, captcha_s

class PostCreativity(Form):
    img = FileField(validators=[])
    b64img = StringField(validators=[Optional(), ])
    mobile = StringField(validators=[Required(), Regexp(mobile_s), ])
    code = StringField(validators=[Required(), Regexp(captcha_s), ])
    def validate(self):
        self.b64img_data = None
        self.b64img_fmt = None
        return Form.validate(self)

    def validate_img(form, field):
        if not field.data and not form.b64img.data:
            raise ValidationError('no img for creativity/application post')

    def validate_b64img(form, field):
        if field.data:
            try:
                mpos = field.data.find(':')
                xpos = field.data.find('/')
                fpos = field.data.find(';')
                dpos = field.data.find(',')
                if -1 in (mpos, xpos, fpos, dpos, ):
                    raise ValidationError('invalid format')
                fmt = field.data[xpos+1:fpos]
                b64data = field.data[dpos+1:]
                import base64
                form.b64img_data = base64.b64decode(b64data)
                form.b64img_fmt = fmt
                return
            except Exception, e:
                logger.error('b64img decode fail: ' + str(e))
                raise ValidationError('invalid b64img')

