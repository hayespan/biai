# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import news_category_service
from ...service import news_service
from ...model.news_category import NewsCategory

@adminbp.route('/news_category')
# @login_required
def l_news_category():
    nc_list = news_category_service.get_categories()
    return admin_response('news_category_list.html',
            news_category_list=nc_list,
            )

@adminbp.route('/news_category/create', methods=['POST', ])
@adminbp.route('/news_category/update', methods=['POST', ])
# @login_required
def cu_news_category():
    from ...form.admin import CUNewsCategoryForm
    form = CUNewsCategoryForm()
    if not form.validate():
        return admin_response(
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
            return admin_response(
                    ret=-2,
                    msg='save NewsCategory img fail.',
                    )
    if id_:
        ret = news_category_service.update_news_category(
                id_, name, file_id, weight,
                )
        return admin_response(ret=ret)
    else:
        ret, new_id = news_category_service.create_news_category(
                name, file_id, weight, 
                )
        return admin_response(ret=ret, id=new_id)

@adminbp.route('/news_category/delete', methods=['POST', ])
# @login_required
def d_news_category():
    from ...form.admin import RDNewsCategoryForm
    form = RDNewsCategoryForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    news_category_service.delete_news_category(id_)
    return admin_response(ret=0)

@adminbp.route('/news_category/<int:id_>')
# @login_required
def r_news_category(id_):
    nc = news_category_service.read_news_category(id_)
    return admin_response('news_category.html',
            news_category=nc,
            )

@adminbp.route('/news')
# @login_required
def l_news():
    page = request.args.get('page', 1)
    n_list = news_service.get_news_list(None, page)
    page_info = news_service.get_news_page_info(None, page)
    return admin_response('news_list.html',
            news_list=n_list,
            page_info=page_info,
            )

@adminbp.route('/news/create', methods=['POST', ])
@adminbp.route('/news/update', methods=['POST', ])
# @login_required
def cu_news():
    from ...form.admin import CUNewsForm
    form = CUNewsForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    title = form.title.data or ''
    content = form.content.data or ''
    news_category_id = form.news_category_id.data or -1 
    if id_:
        ret = news_service.update_news(
                id_, title, content, news_category_id,
                )
        return admin_response(ret=ret)
    else:
        ret, new_id = news_service.create_news(
                title, content, news_category_id, 
                )
        return admin_response(ret=ret, id=new_id)

@adminbp.route('/news/delete', methods=['POST', ])
# @login_required
def d_news():
    from ...form.admin import RDNewsForm
    form = RDNewsForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    news_service.delete_news(id_)
    return admin_response(ret=0)

@adminbp.route('/news/<int:id_>')
# @login_required
def r_news(id_):
    n = news_service.read_news(id_)
    return admin_response('news.html',
            news=n,
            )

