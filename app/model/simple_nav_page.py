# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class SimpleNavPage(db.Model):
    __tablename__ = 'simple_nav_page'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    nav_id = db.Column(db.Integer, db.ForeignKey('nav.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)
    content = db.Column(db.Text)

    nav = db.relationship('Nav', backref=db.backref('simple_nav_page', uselist=False))

    def __init__(self, *args, **kwargs): 
        super(SimpleNavPage, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<SimpleNavPage %d>' % (self.id, )
