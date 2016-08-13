# -*- coding: utf-8 -*-
from .. import db

class Nav(db.Model):
    __tablename__ = 'nav'
    id = db.Column(db.Integer, primary_key=True) 
    meta_name = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(32), nullable=False)
    link = db.Column(db.String(2048), nullable=True)
    def __init__(self, *args, **kwargs): 
        super(Nav, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<Nav %d %s>' % (self.id, self.meta_name)

