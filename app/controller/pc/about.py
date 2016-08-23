# -*- coding: utf-8 -*-

from flask import render_template, request, abort, url_for, session

from . import pcbp 
from ..base_func import *
from ...util.common import logger, json_response, get_now_timestamp
from ...service import nav_service

@pcbp.route('/about', methods=['GET', ])
def about():
    nav = nav_service.get_nav_by_meta_name('about')
    if not nav:
        return abort(404)
    page = nav.simple_nav_page
    return response('about.html',
            page=page,
            )
