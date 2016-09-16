# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import nav_service 
from ...service import simple_nav_page_service
from ... import db
from ...model.simple_nav_page import SimpleNavPage

@adminbp.route('/contact/modify', methods=['GET', 'POST', ])
@login_required
def modify_contact_page():
    if request.method == 'GET':
        nav = nav_service.get_nav_by_meta_name('contact')
        if not nav:
            logger.error('no contact nav, fatal error.')
            abort(404)
        sp = nav.simple_nav_page
        if not sp:
            sp = SimpleNavPage()
            sp.nav = nav
            db.session.add(sp)
            db.session.commit()
        return admin_response('contact.html',
                simple_nav_page=sp,
                )
    elif request.method == 'POST':
        from ...form.admin import USimpleNavPageForm
        form = USimpleNavPageForm()
        if not form.validate():
            return admin_response(
                    ret=-1,
                    msg='input error.' + str(form.errors),
                    )
        id_ = form.id.data
        content = form.content.data
        simple_nav_page_service.update_simple_nav_page(
                id_, content,
                )
        return admin_response(
                ret=0,
                )
    abort(403)

