# -*- coding: utf-8 -*-
from . import pcbp 

from flask import render_template, request, abort, url_for

from ..base_func import *
from ...util.common import logger, json_response
from ...service import product_category_service
from ...service import product_service

@pcbp.route('/product/category/<string:category_name>', methods=['GET', ])
def product_list(category_name):
    product_category_list = product_category_service.get_categories()
    current_category = filter(lambda x:x.name == category_name, product_category_list)
    if current_category:
        current_category = current_category[0]
    else:
        current_category = product_category_list[0] if product_category_list else None
    product_list = product_service.get_product_list(current_category)
    return response('product_list.html',
            current_category=current_category,
            product_category_list=product_category_list,
            product_list=product_list,
            )

@pcbp.route('/product/<int:product_id>', methods=['GET', ])
def product(product_id):
    product_category_list = product_category_service.get_categories()
    product = product_service.get_product(product_id)
    current_category = product.product_categories[0] if product else None
    return response('product.html',
            current_category=current_category,
            product_category_list=product_category_list,
            product=product,
            )
