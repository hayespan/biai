# -*- coding: utf-8 -*-

import json

from datetime import datetime

from .. import db
from ..util.common import AttrDict

association_category_product = db.Table(
        'association_category_product', db.metadata,
        db.Column('product_category_id', db.Integer, db.ForeignKey('product_category.id')),
        db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
        )
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(512), nullable=False)
    pics = db.Column(db.String(2048), nullable=True)
    attrs = db.Column(db.String(2048), nullable=True)
    attr_bits = db.Column(db.Integer, nullable=False, default=0)
    buy_link = db.Column(db.String(1024), nullable=True)
    description = db.Column(db.Text, nullable=True) 

    product_categories = db.relationship('ProductCategory', 
            secondary=association_category_product,
            backref='products')

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return '<Product %d %s>' % (self.id, self.name)

    ATTR_BITS = AttrDict(
            COLOR=1<<0,
            PRICE=1<<1,
            )

    def get_attr_by_bit(self, attr_bit):
        return json.loads(self.attrs)[getattr(ATTR_BITS, attr_bit)] if attr_bit&self.attr_bits else None

    def get_pics(self):
        pics = json.loads(self.pics) if self.pics else []
        abs_path_pics = []
        for i in pics:
            abs_path_pics.append('img/product/' + i)
        return abs_path_pics

