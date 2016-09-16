# -*- coding: utf-8 -*-

import os

from flask import render_template, request, abort
from flask.ext.login import current_user

from ..util.common import logger, json_response, json_error, get_biai_conf
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

def get_cur_nav_meta_name(nav_dict):
    cur_path = request.path
    for k, v in nav_dict.iteritems():
        link = v.link
        if link in cur_path:
            return k
    return None

def get_common_data(is_admin):
    common_data = {}
    if not is_admin:
        common_data['nav_dict'] = nav_service.get_navs()
        common_data['cur_nav_meta_name'] = get_cur_nav_meta_name(common_data['nav_dict'])
        common_data['locale'] = locale_service.get_site_locale()
        succ, common_data['site_name'] = get_biai_conf('site_info', 'site_name')
        succ, common_data['site_domain'] = get_biai_conf('site_info', 'site_domain')
        succ, common_data['site_filing_num'] = get_biai_conf('site_info', 'site_filing_num')
        succ, common_data['company_name'] = get_biai_conf('site_content', 'company_name')
        succ, common_data['service_phone'] = get_biai_conf('site_content', 'service_phone')
        succ, common_data['company_location'] = get_biai_conf('site_content', 'company_location')
    else:
        common_data['current_user'] = current_user
    return common_data

def response(tmpl_path=None, is_admin=False, **kwargs):
    format_ = request.args.get('f', 'html')
    if format_ == 'html':
        if tmpl_path is None:
            abort(404)
        kwargs.update(get_common_data(is_admin))
        if not is_admin:
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

def admin_response(tmpl_path=None, **kwargs):
    return response(tmpl_path, True, **kwargs)

