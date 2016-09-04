# -*- coding: utf-8 -*-
from .. import db


# 网站设置
class WebsiteSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=True)
    url = db.Column(db.String(2048), nullable=False)
    num = db.Column(db.Integer, nullable=True)

    def __init__(self, name, url, num):
        self.name = name
        self.url = url
        self.num = num

    def __repr__(self):
        return '<WebsiteSetting %d>' % (self.id, )

    @staticmethod
    def create():
        db.create_all()


# 管理员设置
class AdminSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(2048), nullable=True)
    password = db.Column(db.String(2048), nullable=True)
    true_name = db.Column(db.String(2048), nullable=False)
    ip = db.Column(db.String(2048), nullable=True)
    login_time = db.Column(db.String(2048), nullable=True)
    add_time = db.Column(db.String(2048), nullable=True)

    def __init__(self, username, password, true_name, ip, login_time, add_time):
        self.username = username
        self.password = password
        self.true_name = true_name
        self.ip = ip
        self.login_time = login_time
        self.add_time = add_time

    def __repr__(self):
        return '<AdminSetting %d>' % (self.id,)

    @staticmethod
    def create():
        db.create_all()

