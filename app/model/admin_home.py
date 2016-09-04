# -*- coding: utf-8 -*-
from .. import db


class ClassifyAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2048), nullable=True)
    img = db.Column(db.String(32), nullable=False)

    def __init__(self, name, img):
        self.name = name
        self.img = img

    def __repr__(self):
        return '<Classify %d>' % (self.id, )

    @staticmethod
    def create():
        db.create_all()


class PosterAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2048), nullable=True)
    img = db.Column(db.String(32), nullable=False)

    def __init__(self, name, img):
        self.name = name
        self.img = img

    def __repr__(self):
        return '<Nav %d>' % (self.id,)

    @staticmethod
    def create():
        db.create_all()


class VideoAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2048), nullable=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<VideoAdmin %d>' % (self.id,)

    @staticmethod
    def create():
        db.create_all()


class NewsAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2048), nullable=True)
    hide = db.Column(db.Boolean, nullable=True)

    def __init__(self, name, hide):
        self.name = name
        self.hide = hide

    def __repr__(self):
        return '<NewsAdmin %d>' % (self.id,)

    @staticmethod
    def create():
        db.create_all()




