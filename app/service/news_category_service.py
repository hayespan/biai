# -*- coding: utf-8 -*-

from .. import db
from ..model.news_category import NewsCategory 

def get_categories():
    return NewsCategory.query.order_by(db.desc('weight'))\
            .order_by(db.asc('id'))\
            .all()

