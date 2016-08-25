# -*- coding: utf-8 -*-

import os

from flask import render_template, request, abort

from ..util.common import logger, json_response, json_error
from ..service import nav_service
from ..service import locale_service

USER_AGENT = ('micromessenger', 'Mobile', 'iPhone', 'Windows Phone', 'UCWEB', 'Fennec', 'Opera Mobi', 'BlackBerry', )

def via_mobile():
    s = request.headers.get('User-Agent')
    if s is None:
        return False
    for i in USER_AGENT:
        if i in s:
            return True
    return False

def get_common_data():
    common_data = {}
    common_data['nav_dict'] = nav_service.get_navs()
    common_data['locale'] = locale_service.get_locale()
    return common_data

def response(tmpl_path=None, **kwargs):
    format_ = request.args.get('f', 'html')
    if format_ == 'html':
        if tmpl_path is None:
            abort(404)
        kwargs.update(get_common_data())
        if not via_mobile():
            tmpl_path = 'pc/' + tmpl_path
        else:
            tmpl_path = 'mb/' + tmpl_path
        return render_template(tmpl_path,
                **kwargs
                )
    elif format_ == 'json':
        if tmpl_path is not None:
            abort(404)
        ret = kwargs.get('ret', 0)
        msg = kwargs.get('msg', 'error')
        if ret >= 0:
            return json_response(**kwargs)
        elif ret < 0:
            return json_error((ret, msg))
    else:
        abort(404)

