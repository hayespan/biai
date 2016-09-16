# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import information_service 
from ...service import news_service
from ...model.information import Information 

@adminbp.route('/information')
@login_required
def l_information():
    information_list= information_service.get_information_list()
    return admin_response('information_list.html',
            information_list=information_list,
            )

@adminbp.route('/information/create', methods=['POST', ])
@login_required
def cu_information():
    from ...form.admin import CInformationForm 
    form = CInformationForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    weight = form.weight.data or 0
    title = form.title.data
    news_id = form.news_id.data
    n = news_service.read_news(news_id)
    if not n:
        return admin_response(
                ret=-2,
                msg='news_id invalid',
                )
    ret, new_id = information_service.create_information(
            title, weight, n,
            )
    return admin_response(ret=ret, id=new_id)

@adminbp.route('/information/delete', methods=['POST', ])
@login_required
def d_information():
    from ...form.admin import DInformationForm 
    form = DInformationForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    information_service.delete_information(id_)
    return admin_response(ret=0)

