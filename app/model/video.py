# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    weight = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(512), nullable=False)
    file_id = db.Column(db.String(512), nullable=False, index=True)
    pic_id = db.Column(db.String(512), nullable=False)

    @classmethod
    def get_file_dir(cls):
        return 'video/mainpage/'

    def get_file_path(self):
        return self.get_file_dir() + self.file_id

    @classmethod
    def get_pic_dir(cls):
        return 'video/pic/'

    def get_pic_path(self):
        return self.get_pic_dir() + self.pic_id

    def __init__(self, *args, **kwargs): 
        super(Video, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<Video %d>' % (self.id, )
