# -*- coding: utf-8 -*-

import os
from datetime import datetime

from .. import db

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(32), nullable=True)
    mobile = db.Column(db.String(32), nullable=False)
    file_id = db.Column(db.String(512), nullable=False)
    draw_file_id = db.Column(db.String(512), nullable=False)
    
    @classmethod
    def get_file_dir(cls):
        return 'img/application/'

    def get_file_path_list(self):
        file_path_list = []
        if self.file_id:
            file_path = os.path.join(self.get_file_dir(), self.file_id)
            file_path_list.append(file_path)
        if self.draw_file_id:
            draw_file_path = os.path.join(self.get_file_dir(), self.draw_file_id)
            file_path_list.append(draw_file_path)
        return file_path_list

    def __init__(self, *args, **kwargs): 
        super(Application, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<Application %d>' % (self.id, )
