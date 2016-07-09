# -*- coding: utf-8 -*-

from .. import db
from ..model.product import Product 

def search_key(key):
    if not key:
        return []
    return Product.query.filter(Product.name.like('%'+key+'%'))\
            .order_by(db.desc('id')).all()
