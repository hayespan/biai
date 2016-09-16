# -*- coding: utf-8 -*-
import json
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import creativity_service 

@adminbp.route('/creativity')
@login_required
def l_creativity():
    ct_list = creativity_service.get_creativity_list()
    return admin_response('creativity_list.html',
            creativity_list=ct_list,
            )

@adminbp.route('/creativity/<int:id_>')
@login_required
def r_creativity(id_):
    cr = creativity_service.read_creativity(id_)
    return admin_response('creativity.html',
            creativity=cr,
            )

@adminbp.route('/creativity/delete', methods=['POST', ])
@login_required
def d_creativity():
    from ...form.admin import RDCreativityForm
    form = RDCreativityForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors)
                )
    id_ = form.id.data
    creativity_service.delete_creativity(id_)
    return admin_response(ret=0)
    
