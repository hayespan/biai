# -*- coding: utf-8 -*-
from .. import db


# 合作加盟
class ParticipateAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2048), nullable=True)
    contact = db.Column(db.String(2048), nullable=True)
    table = db.Column(db.String(2048), nullable=True)

    def __init__(self, name, contact, table):
        self.name = name
        self.contact = contact
        self.table = table

    def __repr__(self):
        return '<OperationAdmin %d>' % (self.id,)

    @staticmethod
    def create():
        db.create_all()


# 人才招聘
class HiringAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2048), nullable=True)
    job = db.Column(db.String(2048), nullable=False)
    contact = db.Column(db.String(2048), nullable=True)
    resume = db.Column(db.String(2048), nullable=True)

    def __init__(self, name, job, contact, resume):
        self.name = name
        self.job = job
        self.contact = contact
        self.resume = resume

    def __repr__(self):
        return '<HiringAdmin %d>' % (self.id,)

    @staticmethod
    def create():
        db.create_all()
