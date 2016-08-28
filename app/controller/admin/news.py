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

@adminbp.route('/news')
def l_news():
    page = request.args.get('page', 1)
    n_list = news_service.get_news_list(None, page)
    page_info = news_service.get_news_page_info(None, page)
    return response('news_list.html',
            news_list=n_list,
            page_info=page_info,
            )

@adminbp.route('/news/create', methods=['POST', ])
@adminbp.route('/news/update', methods=['POST', ])
def cu_news():
    from ...form.admin import CUNewsForm
    form = CUNewsForm()
    if not form.validate():
        return response(
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
        return response(ret=ret)
    else:
        ret, new_id = news_service.create_news(
                title, content, news_category_id, 
                )
        return response(ret=ret, id=new_id)

@adminbp.route('/news/delete', methods=['POST', ])
def d_news():
    from ...form.admin import RDNewsForm
    form = RDNewsForm()
    if not form.validate():
        return response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    news_service.delete_news(id_)
    return response(ret=0)

@adminbp.route('/news/<int:id_>')
def r_news(id_):
    from ...form.admin import RDNewsForm
    form = RDNewsForm()
    if not form.validate():
        abort(404)
    id_ = form.id.data
    n = news_service.read_news(id_)
    return response('news.html',
            news=c,
            )

