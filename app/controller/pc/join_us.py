# -*- coding: utf-8 -*-
from flask import render_template, request, abort, url_for, session

from . import pcbp 
from ..base_func import *
from ...util.common import logger, json_response, get_now_timestamp

@pcbp.route('/join_us', methods=['GET', ])
def join_us():
    nav = nav_service.get_nav_by_meta_name('join_us')
    if not nav:
        return abort(404)
    page = nav.simple_nav_page
    return response('pc/join_us.html',
            page=page,
            )

@pcbp.route('/join_us/cooperation/post', methods=['POST', ])
def cooperation_post():
    pass
