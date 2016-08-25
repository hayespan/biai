# -*- coding: utf-8 -*-

from flask import session

def get_locale():
    lc = session.get('locale', 'zh_CN')
    return lc

