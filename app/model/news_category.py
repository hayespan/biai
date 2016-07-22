# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class NewsCategory(db.Model):
    __tablename__ = 'news_category'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(512), nullable=False)
    file_id = db.Column(db.String(32), nullable=True)
    weight = db.Column(db.Integer, nullable=False, default=0)

    def get_file_path(self):
        return 'img/news_category/' + self.file_id

    def __init__(self, *args, **kwargs): 
        super(NewsCategory, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<NewsCategory %d %s>' % (self.id, self.name)
