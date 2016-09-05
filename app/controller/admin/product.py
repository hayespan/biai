# -*- coding: utf-8 -*-
import json
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import product_category_service
from ...service import product_service
from ...model.product_category import ProductCategory 
from ...model.product import Product

@adminbp.route('/product_category')
@login_required
def l_product_category():
    pc_list = product_category_service.get_categories()
    return admin_response('product_category_list.html',
            product_category_list=pc_list,
            )

@adminbp.route('/product_category/create', methods=['POST', ])
@adminbp.route('/product_category/update', methods=['POST', ])
@login_required
def cu_product_category():
    from ...form.admin import CUProductCategoryForm
    form = CUProductCategoryForm()
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
                ProductCategory.get_file_dir())
        if not succ:
            return admin_response(
                    ret=-2,
                    msg='save ProductCategory img fail.',
                    )
    if id_:
        ret = product_category_service.update_product_category(
                id_, name, file_id, weight,
                )
        return admin_response(ret=ret)
    else:
        ret, new_id = product_category_service.create_product_category(
                name, file_id, weight, 
                )
        return admin_response(ret=ret, id=new_id)

@adminbp.route('/product_category/delete', methods=['POST', ])
@login_required
def d_product_category():
    from ...form.admin import RDProductCategoryForm
    form = RDProductCategoryForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    product_category_service.delete_product_category(id_)
    return admin_response(ret=0)

@adminbp.route('/product_category/<int:id_>')
@login_required
def r_product_category(id_):
    pc = product_category_service.read_product_category(id_)
    return admin_response('product_category.html',
            product_category=pc,
            )

@adminbp.route('/product')
@login_required
def l_product():
    page = request.args.get('page', 1)
    p_list = product_service.get_product_list(None, page)
    page_info = product_service.get_product_page_info(None, page)
    return admin_response('product_list.html',
            product_list=p_list,
            page_info=page_info,
            )

@adminbp.route('/product/create', methods=['POST', ])
@adminbp.route('/product/update', methods=['POST', ])
@login_required
def cu_product():
    from ...form.admin import CUProductForm
    form = CUProductForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    name = form.name.data or ''
    attrs_ = form.attrs.data or '{}'
    oth_attrs_ = form.oth_attrs.data or '{}'
    category_ids = form.category_ids.data or '[]'
    file_ids = form.file_ids.data or '[]'
    buy_link = form.buy_link.data or None
    description = form.description.data or ''

    attrs = json.loads(attrs_)
    oth_attrs = json.loads(oth_attrs_)
    file_id_list = json.loads(file_ids)
    category_id_list = json.loads(category_ids)

    if id_:
        ret = product_service.update_product(
                id_, name, attrs, oth_attrs, 
                buy_link, description, category_id_list, 
                file_id_list,
                )
        return admin_response(ret=ret)
    else:
        ret, new_id = product_service.create_product(
                name, attrs, oth_attrs, 
                buy_link, description, category_id_list, 
                file_id_list,
                )
        return admin_response(ret=ret, id=new_id)

@adminbp.route('/product/delete', methods=['POST', ])
@login_required
def d_product():
    from ...form.admin import RDProductForm
    form = RDProductForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    product_service.delete_product(id_)
    return admin_response(ret=0)

@adminbp.route('/product/<int:id_>')
@login_required
def r_product(id_):
    p = product_service.read_product(id_)
    pcl = product_category_service.get_categories()
    return admin_response('product.html',
            product=p,
            product_categories=pcl,
            )

@adminbp.route('/product/upload', methods=['POST', ])
@login_required
def upload_product_pic():
    from ...form.admin import UploadProductPicForm
    form = UploadProductPicForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error',
                )
    file_id = ''
    if form.pic.data:
        succ, file_id = save_form_file(form.pic.data, Product.get_file_dir())
        if not succ:
            return admin_response(
                    ret=-2,
                    msg='save file fail',
                    )
    return admin_response(
            ret=0,
            file_id=file_id,
            )

