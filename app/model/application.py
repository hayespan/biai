# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(32), nullable=True)
    mobile = db.Column(db.String(32), nullable=False)
    file_id = db.Column(db.String(32), nullable=False)
    
    def get_file_path(self):
        return 'img/application/' + self.file_id

    def __init__(self, *args, **kwargs): 
        super(Application, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<Application %d %s>' % (self.id, self.mobile)
