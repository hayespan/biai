# -*- coding: utf-8 -*-

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from flask.ext.login import UserMixin

from .. import db

class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(32), nullable=False, index=True) 
    password_hash = db.Column(db.String(128), nullable=False) 
    is_admin = db.Column(db.Boolean, nullable=False, default=False) 
    is_active = db.Column(db.Boolean, nullable=False, default=True) 
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

    def __init__(self, *args, **kwargs): 
        super(Admin, self).__init__(*args, **kwargs) 

    @property 
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password) 

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return self.is_active
        
    def __repr__(self):
        return '<User %d>' % (self.id, )


from flask.ext.login import AnonymousUserMixin
class MyAnonymousUser(AnonymousUserMixin):
    is_admin = False

