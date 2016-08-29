# -*- coding: utf-8 -*-
from flask import session, current_app
from ..util.common import logger, get_now_timestamp

def check_captcha(code_):
    code = session.get('captcha_mobile_code', '')
    expire = session.get('captcha_mobile_expire', 0)
    correct = current_app.config['DEBUG'] or \
            (code == code_ and expire>get_now_timestamp())
    return correct

