# -*- coding: utf-8 -*-

from flask import render_template, request, abort, url_for, session

from . import pcbp 
from ..base_func import response
from ...util.common import logger, json_response, get_now_timestamp
from ...service import nav_service

@pcbp.route('/contact', methods=['GET', ])
def contact():
    nav = nav_service.get_nav_by_meta_name('contact')
    if not nav:
        return abort(404)
    page = nav.simple_nav_page
    return response('contact.html',
            page=page,
            )
