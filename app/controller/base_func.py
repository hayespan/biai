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

<<<<<<< HEAD
=======
def get_cur_nav_meta_name(nav_dict):
    cur_path = request.path
    for k, v in nav_dict.iteritems():
        link = v.link
        if link in cur_path:
            return k
    return None
>>>>>>> 4b3b4470e40d8a8c7dd177302192a4718ae71d3d

def get_common_data():
    common_data = {}
    common_data['nav_dict'] = nav_service.get_navs()
    common_data['cur_nav_meta_name'] = get_cur_nav_meta_name(common_data['nav_dict'])
    common_data['locale'] = locale_service.get_site_locale()
    return common_data

<<<<<<< HEAD

def response(tmpl_path=None, **kwargs):
=======
def response(tmpl_path=None, admin=False, **kwargs):
>>>>>>> 4b3b4470e40d8a8c7dd177302192a4718ae71d3d
    format_ = request.args.get('f', 'html')
    if format_ == 'html':
        if tmpl_path is None:
            abort(404)
        kwargs.update(get_common_data())
        if not admin:
            if not via_mobile():
                tmpl_path = 'pc/' + tmpl_path
            else:
                tmpl_path = 'mb/' + tmpl_path
        else:
            tmpl_path = 'admin/' + tmpl_path
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

