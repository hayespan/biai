# -*- coding: utf-8 -*-
from .. import db

class SubNav(db.Model):
    __tablename__ = 'subnav'
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(32), nullable=False)
    link = db.Column(db.String(2048), nullable=True)
    nav_id = db.Column(db.Integer, db.ForeignKey('nav.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    nav = db.relationship('Nav', backref=db.backref('subnavs', uselist=True))

    def __init__(self, *args, **kwargs): 
        super(SubNav, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<SubNav %d>' % self.id

