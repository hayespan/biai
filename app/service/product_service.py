# -*- coding: utf-8 -*-

from .. import db
from ..model.product import Product 
from ..util.common import page_info


def search_key(key):
    if not key:
        return []
    return Product.query.filter(Product.name.like('%'+key+'%'))\
            .order_by(db.desc('id')).all()

<<<<<<< HEAD

def get_product_list(category):
    products = category.products if category else Product.query.all()
    products = sorted(products, lambda a,b:a.id>b.id)
=======
def get_product_page_info(category, cur, per=20):
    query = category.products if category else Product.query
    tot = query.count()
    return page_info(tot, per, cur)

def get_product_list(category, page, per=20):
    query = category.products if category else Product.query
    offset = (page-1)*per
    offset = 0 if offset < 0 else offset
    products = query.order_by(db.desc('id')).offset(offset).limit(per).all()
>>>>>>> 4b3b4470e40d8a8c7dd177302192a4718ae71d3d
    return products


def get_product(product_id):
    return Product.query.filter_by(id=product_id).first()

