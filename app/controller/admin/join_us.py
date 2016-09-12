# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import cooperation_service 
from ...service import nav_service
from ...service import simple_nav_page_service
from ...model.simple_nav_page import SimpleNavPage
from ... import db

@adminbp.route('/cooperation')
# @login_required
def l_cooperation():
    cpl= cooperation_service.get_cooperations()
    return admin_response('cooperation_list.html',
            cooperation_list=cpl,
            )

@adminbp.route('/cooperation/<int:cooperation_id>')
# @login_required
def r_cooperation(cooperation_id):
    cp = cooperation_service.read_cooperation(cooperation_id)
    return admin_response('cooperation.html',
            cooperation=cp,
            )

@adminbp.route('/cooperation/delete', methods=['POST', ])
# @login_required
def d_cooperation():
    from ...form.admin import DCooperationForm 
    form = DCooperationForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    cooperation_service.delete_cooperation(id_)
    return admin_response(ret=0)

@adminbp.route('/join_us/modify', methods=['GET', 'POST', ])
# @login_required
def modify_join_us_page():
    if request.method == 'GET':
        nav = nav_service.get_nav_by_meta_name('join_us')
        if not nav:
            logger.error('no join_us nav, fatal error.')
            abort(404)
        sp = nav.simple_nav_page
        if not sp:
            sp = SimpleNavPage()
            sp.nav = nav
            db.session.add(sp)
            db.session.commit()
        return admin_response('join_us.html',
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
