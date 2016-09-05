# -*- coding: utf-8 -*-

import datetime
from .. import db
from ..model.product import Product 
from ..util.common import page_info
from ..model.product_category import ProductCategory


def search_key(key):
    if not key:
        return []
    return Product.query.filter(Product.name.like('%'+key+'%'))\
            .order_by(db.desc('id')).all()

def get_product_page_info(category, cur, per=20):
    query = category.products if category else Product.query
    tot = query.count()
    return page_info(tot, per, cur)

def get_product_list(category, page, per=20):
    query = category.products if category else Product.query
    offset = (page-1)*per
    offset = 0 if offset < 0 else offset
    products = query.order_by(db.desc('id')).offset(offset).limit(per).all()
    return products

def get_product(product_id):
    return Product.query.filter_by(id=product_id).first()

def create_product(name, attrs, oth_attrs, 
        buy_link, description, category_id_list, file_id_list,  
        ):
    p = Product(
            name=name,
            buy_link=buy_link,
            description=description,
            )
    p.set_attrs(attrs)
    p.set_oth_attrs(oth_attrs)
    p.set_pics(file_id_list)
    reset_product_category(p, category_id_list)
    db.session.add(p)
    db.session.commit()
    return 0, p.id

def update_product(id_, name, attrs, oth_attrs, 
        buy_link, description, category_id_list, file_id_list,  
        ):
    p = Product.query.filter_by(id=id_).first()
    if not p:
        return -1
    p.modify_time = datetime.datetime.now()
    p.name = name 
    p.buy_link = buy_link
    p.description = description
    p.set_attrs(attrs)
    p.set_oth_attrs(oth_attrs)
    p.set_pics(file_id_list)
    reset_product_category(p, category_id_list)
    db.session.add(p)
    return 0

def reset_product_category(p, category_id_list):
    ori_pcl = p.product_categories.all()
    for i in ori_pcl:
        p.product_categories.remove(i)
    for i in category_id_list:
        pc = ProductCategory.query.filter_by(id=i).first()
        if pc:
            p.product_categories.append(pc)

def read_product(id_):
    p = Product.query.filter_by(id=id_).first()
    return p

def delete_product(id_):
    p = Product.query.filter_by(id=id_).first()
    if p:
        db.session.delete(p)

