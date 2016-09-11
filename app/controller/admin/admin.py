# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import admin_service 
from ...service.admin_service import Admin 

@adminbp.route('/admin')
@login_required
def l_admin():
    admin_list= admin_service.get_admins()
    return admin_response('admin_list.html',
            admin_list=admin_list,
            )

@adminbp.route('/admin/create', methods=['POST', ])
@login_required
def c_admin():
    from ...form.admin import CAdminForm 
    form = CAdminForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    username = form.username.data
    password = form.password.data
    real_name = form.real_name.data

    ret, new_id = admin_service.create_admin(
            username, password, real_name,
            )
    return admin_response(ret=ret, id=new_id)


@adminbp.route('/admin/delete', methods=['POST', ])
@login_required
def d_admin():
    from ...form.admin import DAdminForm 
    form = DAdminForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    admin_service.delete_admin(id_)
    return admin_response(ret=0)

