# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class Information(db.Model):
    __tablename__ = 'information'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(1024), nullable=False)
    weight = db.Column(db.Integer, nullable=False, default=0)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)

    news = db.relationship('News', backref=db.backref('information', lazy='dynamic'))

    def __init__(self, *args, **kwargs): 
        super(Information, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<Information %d>' % (self.id, )
