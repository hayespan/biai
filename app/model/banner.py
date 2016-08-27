# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class Banner(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    weight = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(512), nullable=False)
    file_id = db.Column(db.String(512), nullable=False, index=True)

    def get_file_path(self):
        return 'img/banner/' + self.file_id

    def __init__(self, *args, **kwargs): 
        super(Banner, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<Banner %d>' % (self.id, )
