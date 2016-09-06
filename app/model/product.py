# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from datetime import datetime

from .. import db
from ..util.common import AttrDict

association_category_product = db.Table(
        'association_category_product', db.metadata,
        db.Column('product_category_id', db.Integer, db.ForeignKey('product_category.id')),
        db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
        db.UniqueConstraint('product_category_id', 'product_id'),
        )
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(512), nullable=False)
    pics = db.Column(db.String(2048), nullable=True)
    attrs = db.Column(db.String(2048), nullable=False)
    oth_attrs = db.Column(db.String(2048), nullable=False)
    buy_link = db.Column(db.String(1024), nullable=True)
    description = db.Column(db.Text, nullable=True) 

    product_categories = db.relationship('ProductCategory', 
            secondary=association_category_product,
            backref=db.backref('products', lazy='dynamic'),
            lazy='dynamic',
            )

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return '<Product %d>' % (self.id, )

    def set_attrs(self, attrs):
        attrs = attrs or []
        self.attrs = json.dumps(attrs)

    def get_attrs(self):
    	attrs = json.loads(self.attrs) if self.attrs else []
    	return attrs

    def set_oth_attrs(self, oth_attrs):
    	oth_attrs = oth_attrs or []
    	self.oth_attrs = json.dumps(oth_attrs)

    def get_oth_attrs(self):
    	oth_attrs = json.loads(self.oth_attrs) if self.oth_attrs else []
    	return oth_attrs
    	
    def get_pics(self):
        pics = json.loads(self.pics) if self.pics else []
        abs_path_pics = []
        for i in pics:
            abs_path_pics.append(self.get_file_dir() + i)
        return abs_path_pics
    
    def set_pics(self, file_id_list):
        file_id_list = file_id_list or []
        file_id_list_ = []
        for i in file_id_list:
            file_id = i.rsplit('/')
            file_id_list_.append(file_id)
        self.file_id_list = file_id_list_

    @classmethod
    def get_file_dir(cls):
        return 'img/product/'

