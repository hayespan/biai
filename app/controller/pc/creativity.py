# -*- coding: utf-8 -*-
from . import pcbp 

from flask import render_template, request, abort, url_for

from ..base_func import *
from ...util.common import logger, json_response, save_form_file
from ...model.application import Application

@pcbp.route('/creativity')
def creativity():
    return response('pc/creativity.html')

@pcbp.route('/creativity/post', methods=['POST', ])
def post_creativity():
    from ...form.creativity import PostCreativity
    form = PostCreativity()
    if not form.validate():
        return response(
                ret=-1,
                msg='input error',
                )
    succ, _ = save_form_file(form.img.data, Application.get_file_dir())
    if not succ:
        return response(
                ret=-2,
                msg='save file fail',
                )
    file_id = _
    application = Application(
            mobile=form.mobile.data,
            file_id=file_id,
            )
    db.session.add(application)
    return response(
            ret=0,
            )
