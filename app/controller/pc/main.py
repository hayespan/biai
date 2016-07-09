# -*- coding: utf-8 -*-
from . import pcbp 

from flask import render_template, request, abort, url_for

from ..base_func import *
from ...util.common import logger, json_response
from ...service import nav_service
from ...service import banner_service
from ...service import product_category_service
from ...service import video_service
from ...service import consult_service
from ...service import product_service

@pcbp.route('/search', methods=['GET', 'POST', ])
def search():
    from ...form.main import SearchForm
    form = SearchForm()
    key = ''
    if form.validate():
        key = form.key.data()
    product_list = product_service.search_key(key)
    return response('pc/search_product_list.html',
            product_list=product_list,
            )

@pcbp.route('/')
def index():
    banner_list = banner_service.get_banners()
    product_category_list = product_category_service.get_category_list()
    video_list = video_service.get_videos()
    consult_page_content = consult_service.get_page_content()
    return response('pc/main_page.html', 
            banner_list=banner_list,
            product_category_list=product_category_list,
            video_list=video_list,
            consult_page_content=consult_page_content,
            )

