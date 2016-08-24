# -*- coding: utf-8 -*-

from .. import db
from ..model.product import Product 
from ..util.common import page_info

def search_key(key):
    if not key:
        return []
    return Product.query.filter(Product.name.like('%'+key+'%'))\
            .order_by(db.desc('id')).all()

def get_product_page_info(category, cur, per=20):
    query = category.products if category else Product.query
    tot = query.count()
    return page_info(tot, per, cur)

def get_product_list(category, page):
    query = category.products if category else Product.query
    products = query.order_by(db.desc('id')).all()
    return products

def get_product(product_id):
    return Product.query.filter_by(id=product_id).first()

