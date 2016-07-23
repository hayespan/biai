# -*- coding: utf-8 -*-

from .. import db
from ..model.product import Product 

def search_key(key):
    if not key:
        return []
    return Product.query.filter(Product.name.like('%'+key+'%'))\
            .order_by(db.desc('id')).all()

def get_product_list(category):
    query = category.products.query if category else Product.query
    return query.order_by(db.desc('id'))\
            .all()

def get_product(product_id):
    return Product.query.filter_by(id=product_id).first()

