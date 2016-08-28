# -*- coding: utf-8 -*-

import datetime

from .. import db
from ..model.news_category import NewsCategory 

def get_categories():
    return NewsCategory.query.order_by(db.desc('weight'))\
            .order_by(db.asc('id'))\
            .all()

def create_news_category(name, file_id, weight):
    nc = NewsCategory(
            name=name,
            file_id=file_id,
            weight=weight,
            )
    db.session.add(nc)
    db.session.commit()
    return 0, nc.id

def update_news_category(id_, name, file_id, weight):
    nc = NewsCategory.query.filter_by(id=id_).first()
    if not nc:
        return -1
    nc.name = name
    nc.file_id = file_id
    nc.weight = nc.weight
    db.session.add(nc)
    return 0

def read_news_category(id_):
    nc = NewsCategory.query.filter_by(id=id_).first()
    return nc

def delete_news_category(id_):
    nc = NewsCategory.query.filter_by(id=id_).first()
    if nc:
        db.session.delete(nc)

