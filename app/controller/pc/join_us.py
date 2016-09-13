# -*- coding: utf-8 -*-
from flask import render_template, request, abort, url_for, session

from . import pcbp 
from ... import db
from ..base_func import response
from ...util.common import logger, json_response, get_now_timestamp
from ...service import captcha_service
from ...service import nav_service
from ...service import cooperation_service 
from ...model.cooperation import Cooperation

@pcbp.route('/join_us', methods=['GET', ])
def join_us():
    nav = nav_service.get_nav_by_meta_name('join_us')
    if not nav:
        return abort(404)
    page = nav.simple_nav_page
    return response('join_us.html',
            page=page,
            )

@pcbp.route('/join_us/cooperation/post', methods=['POST', ])
def cooperation_post():
    from ...form.join_us import CooperationForm
    form = CooperationForm()
    if not form.validate():
        return response(
                ret=-1,
                msg=str(form.errors),
                )
    if not captcha_service.check_captcha(form.code.data):
        return response(
                ret=-3,
                msg='captcha code error',
                )
    ret, new_id = cooperation_service.create_cooperation(
            form.name.data,
            form.contact.data,
            form.zone.data,
            form.shop_range.data,
            form.develop_plan.data,
            form.cooperation_intention.data,
            )
    return response(
            ret=ret,
            new_id=new_id,
            )

