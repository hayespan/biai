# -*- coding: utf-8 -*-

from .. import db
from ..model.product_category import ProductCategory

def get_categories():
    return ProductCategory.query.order_by(db.desc('weight')).order_by(db.asc('id')).all()
