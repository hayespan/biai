# -*- coding: utf-8 -*-

from .. import db
from ..model.news_category import NewsCategory 
from ..model.news import News

def get_news_list(category):
    news = category.news if category else News.query.all()
    news = sorted(news, lambda a,b:a.id>b.id)
    return news

def get_news(news_id):
    return News.query.filter_by(id=news_id).first()

