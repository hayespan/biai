# -*- coding: utf-8 -*-

from .. import db
from ..model.news_category import NewsCategory 
from ..model.news import News
from ..util.common import page_info
from .news_category_service import read_news_category

def get_news_list(category, page, per=20):
    query = category.news if category else News.query
    offset = (page-1)*per
    offset = 0 if offset < 0 else offset
    news = query.order_by(db.desc('id')).offset(offset).limit(per).all()
    return news

def get_news_page_info(category, cur, per=20):
    query = category.news if category else News.query
    tot = query.count()
    return page_info(tot, per, cur)

def get_news(news_id):
    return News.query.filter_by(id=news_id).first()

def create_news(title, content, news_category_id):
    n = News(
            title=title,
            content=content,
            )
    nc = read_news_category(news_category_id)
    n.news_category = nc
    db.session.add(n)
    db.session.commit()
    return 0, n.id

def update_news(title, content, news_category_id):
    n = News.query.filter_by(id=id_).first()
    if not n:
        return -1
    n.title = title
    n.content = content
    nc = read_news_category(news_category_id)
    n.news_category = nc
    db.session.add(nc)
    return 0

def read_news(id_):
    n = News.query.filter_by(id=id_).first()
    return nc

def delete_news(id_):
    n = News.query.filter_by(id=id_).first()
    if n:
        db.session.delete(nc)

