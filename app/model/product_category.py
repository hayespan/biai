# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class ProductCategory(db.Model):
    __tablename__ = 'product_category'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(512), nullable=False)
    file_id = db.Column(db.String(512), nullable=True)
    weight = db.Column(db.Integer, nullable=False, default=0)

    @classmethod
    def get_file_dir(cls):
        return 'img/product_category/'

    def get_file_path(self):
        if self.file_id:
            path = self.get_file_dir() + self.file_id 
        else:
            path = None
        return path

    def __init__(self, *args, **kwargs): 
        super(ProductCategory, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<ProductCategory %d>' % (self.id, )
