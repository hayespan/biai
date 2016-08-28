# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for

from ..base_func import *
from ...util.common import logger, json_response
from ...service import news_category_service
from ...service import news_service

@adminbp.route('/news_category')
def l_news_category():
    nc_list = news_category_service.get_categories()
    return response('news_category_list.html',
            news_category_list=nc_list,
            )

@adminbp.route('/news_category/create', methods=['POST', ])
@adminbp.route('/news_category/update', methods=['POST', ])
def cu_news_category():
    from ...form.admin import CUNewsCategoryForm
    form = CUNewsCategoryForm()
    if not form.validate():
        return response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    name = form.name.data or ''
    file_id = None
    weight = form.weight.data or 0
    if form.img.data:
        succ, file_id = save_form_file(form.img.data,
                NewsCategory.get_file_dir())
        if not succ:
            return response(
                    ret=-2,
                    msg='save NewsCategory img fail.',
                    )
    if id_:
        ret = news_category_service.update_news_category(
                id_, name, file_id, weight,
                )
        return response(ret=ret)
    else:
        ret, new_id = news_category_service.create_news_category(
                name, file_id, weight, 
                )
        return response(ret=ret, id=new_id)

@adminbp.route('/news_category/delete', methods=['POST', ])
def d_news_category():
    from ...form.admin import RDNewsCategoryForm
    form = RDNewsCategoryForm()
    if not form.validate():
        return response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    news_category_service.delete_news_category(id_)
    return response(ret=0)

@adminbp.route('/news_category/<int:id_>')
def r_news_category(id_):
    from ...form.admin import RDNewsCategoryForm
    form = RDNewsCategoryForm()
    if not form.validate():
        abort(404)
    id_ = form.id.data
    nc = news_category_service.read_news_category(id_)
    return response('news_category.html',
            news_category=nc,
            )

