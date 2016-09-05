# -*- coding: utf-8 -*-

import datetime
from .. import db
from ..model.creativity import Creativity

def get_creativity_list():
    return Creativity.query.order_by(db.desc('id')).all()

def read_creativity(id_):
    cr = Creativity.query.filter_by(id=id_).first()
    return cr

def delete_creativity(id_):
    cr = Creativity.query.filter_by(id=id_).first()
    if cr:
        db.session.delete(cr)

