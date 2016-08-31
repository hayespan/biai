# -*- coding: utf-8 -*-

from .. import db
from ..model.product import Product 


def search_key(key):
    if not key:
        return []
    return Product.query.filter(Product.name.like('%'+key+'%'))\
            .order_by(db.desc('id')).all()


def get_product_list(category):
    products = category.products if category else Product.query.all()
    products = sorted(products, lambda a,b:a.id>b.id)
    return products


def get_product(product_id):
    return Product.query.filter_by(id=product_id).first()

