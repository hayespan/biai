# -*- coding: utf-8 -*-

from .. import db
from ..model.news_category import NewsCategory 
from ..model.news import News

def get_news_list(category):
    query = category.news.query if category else News.query
    return query.order_by(db.desc('id'))\
            .all()

def get_news(news_id):
    return News.query.filter_by(id=news_id).first()

