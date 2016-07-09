# -*- coding: utf-8 -*-

from flask import render_template, request, abort

from ..util.common import logger, json_response, json_error
from ..service import nav_service

def get_common_data():
    common_data = {}
    common_data['nav_dict'] = nav_service.get_navs()
    return common_data

def response(tmpl_path=None, **kwargs):
    format_ = request.args.get('f', 'html')
    if format_ == 'html':
        if tmpl_path is None:
            abort(404)
        kwargs.update(get_common_data())
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

