# -*- coding: utf-8 -*-
import os

from . import pcbp 

from flask import render_template, request, abort, url_for

from ... import db
from ..base_func import *
from ...util.common import logger, json_response, save_form_file, gen_random_filename
from ...model.application import Application
from ...service import captcha_service

@pcbp.route('/creativity')
def creativity():
    return response('creativity.html')

@pcbp.route('/creativity/post', methods=['POST', ])
def post_creativity():
    from ...form.creativity import PostCreativity
    form = PostCreativity()
    if not form.validate():
        print form.errors['mobile'][0]
        return response(
                ret=-1,
                msg='input error',
                )
    # if not captcha_service.check_captcha(form.code.data):
        # return response(
                # ret=-3,
                # msg='captcha code error',
                # )
    file_id, draw_file_id = '', ''
    if form.img.data:
        succ, _ = save_form_file(form.img.data, Application.get_file_dir())
        if not succ:
            return response(
                    ret=-2,
                    msg='save file fail',
                    )
        file_id = _
    if form.b64img_data:
        succ, _ = save_form_file(form.b64img_data, Application.get_file_dir(), gen_random_filename(form.b64img_fmt))
        if not succ:
            return response(
                    ret=-3,
                    msg='save draw file fail',
                    )
        draw_file_id = _
    application = Application(
            mobile=form.mobile.data,
            file_id=file_id,
            draw_file_id=draw_file_id,
            )
    db.session.add(application)
    return response(
            ret=0,
            )

