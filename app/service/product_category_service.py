# -*- coding: utf-8 -*-

from .. import db
from ..model.product_category import ProductCategory

def get_categories():
    return ProductCategory.query.order_by(db.desc('weight')).order_by(db.asc('id')).all()

def create_product_category(name, file_id, weight):
    pc = ProductCategory(
            name=name,
            file_id=file_id,
            weight=weight,
            )
    db.session.add(pc)
    db.session.commit()
    return 0, pc.id

def update_product_category(id_, name, file_id, weight):
    pc = ProductCategory.query.filter_by(id=id_).first()
    if not pc:
        return -1
    pc.name = name
    if file_id:
        pc.file_id = file_id
    pc.weight = weight
    db.session.add(pc)
    return 0

def read_product_category(id_):
    pc = ProductCategory.query.filter_by(id=id_).first()
    return pc

def delete_product_category(id_):
    pc = ProductCategory.query.filter_by(id=id_).first()
    if pc:
        db.session.delete(pc)

