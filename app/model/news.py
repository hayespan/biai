# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(1024), nullable=False)
    content = db.Column(db.Text)
    news_category_idi = db.Column(db.Integer, db.ForeignKey('news_category.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)

    news_category = db.relationship('NewsCategory', backref=db.backref('news', lazy='dynamic'))

    def __init__(self, *args, **kwargs): 
        super(News, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<News %d>' % (self.id, )
