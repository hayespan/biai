# -*- coding: utf-8 -*-
from . import pcbp 

from flask import render_template, request, abort, url_for

from ..base_func import response
from ...util.common import logger, json_response
from ...service import news_category_service
from ...service import news_service

@pcbp.route('/news', defaults={'category_name': None, 'page': 1}, methods=['GET', ])
@pcbp.route('/news/category/<string:category_name>/<int:page>', methods=['GET', ])
def news_list(category_name, page):
    news_category_list = news_category_service.get_categories()
    current_category = filter(lambda x:x.name == category_name, news_category_list)
    if current_category:
        current_category = current_category[0]
    else:
        current_category = news_category_list[0] if news_category_list else None
    news_list = news_service.get_news_list(current_category, page)
    page_info = news_service.get_news_page_info(current_category, page)
    return response('news_list.html',
            current_category=current_category,
            news_category_list=news_category_list,
            news_list=news_list,
            page_info=page_info,
            )

@pcbp.route('/news/<int:news_id>', methods=['GET', ])
def news(news_id):
    news_category_list = news_category_service.get_categories()
    news = news_service.get_news(news_id)
    current_category = news.news_category if news else None
    return response('news.html',
            current_category=current_category,
            news_category_list=news_category_list,
            news=news,
            )
