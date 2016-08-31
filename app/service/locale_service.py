# -*- coding: utf-8 -*-

from flask import session, current_app

def get_locale():
    lc = session.get('locale', 'zh_CN')
    return lc

def get_site_locale():
    from ..util.common import get_biai_conf
    return get_biai_conf('site_info', 'site_locale')

