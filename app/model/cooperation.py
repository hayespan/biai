# -*- coding: utf-8 -*-

from datetime import datetime

from .. import db

class Cooperation(db.Model):
    __tablename__ = 'cooperation'
    id = db.Column(db.Integer, primary_key=True) 
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(32), nullable=True)
    mobile = db.Column(db.String(32), nullable=True)
    zone = db.Column(db.String(512), nullable=True)
    shop_range = db.Column(db.String(1024), nullable=True)
    develop_plan = db.Column(db.Text, nullable=True)
    cooperation_intention = db.Column(db.Text, nullable=True)

    def __init__(self, *args, **kwargs): 
        super(Cooperation, self).__init__(*args, **kwargs) 

    def __repr__(self):
        return '<Cooperation %d>' % (self.id, )
