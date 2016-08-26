# -*- coding: utf-8 -*-

from .. import db
from ..model.news_category import NewsCategory 
from ..model.news import News
from ..util.common import page_info

def get_news_list(category, page):
    query = category.news if category else News.query
    news = query.order_by(db.desc('id')).all()
    return news

def get_news_page_info(category, cur, per=20):
    query = category.news if category else News.query
    tot = query.count()
    return page_info(tot, per, cur)

def get_news(news_id):
    return News.query.filter_by(id=news_id).first()

