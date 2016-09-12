# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import banner_service 
from ...model.banner import Banner

@adminbp.route('/banner')
# @login_required
def l_banner():
    banner_list= banner_service.get_banners()
    return admin_response('banner_list.html',
            banner_list=banner_list,
            )

@adminbp.route('/banner/create', methods=['POST', ])
# @login_required
def cu_banner():
    from ...form.admin import CBannerForm
    form = CBannerForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    weight = form.weight.data or 0
    name = form.name.data or ''
    succ, file_id = save_form_file(form.pic.data, 
            Banner.get_file_dir())
    if not succ:
        return admin_response(
                ret=-2,
                msg='save NewsCategory img fail.',
                )
    ret, new_id = banner_service.create_banner(
            weight, name, file_id,
            )
    return admin_response(ret=ret, id=new_id)


@adminbp.route('/banner/delete', methods=['POST', ])
# @login_required
def d_banner():
    from ...form.admin import DBannerForm 
    form = DBannerForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    banner_service.delete_banner(id_)
    return admin_response(ret=0)

