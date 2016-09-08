# -*- coding: utf-8 -*-

from .. import db
from ..model.banner import Banner

def get_banners():
    return Banner.query.order_by(db.desc('weight'))\
            .order_by(db.desc('id')).all()

def create_banner(weight, name, file_id):
    b = Banner(
            weight=weight,
            name=name,
            file_id=file_id,
            )
    db.session.add(b)
    db.session.commit()
    return 0, b.id

def delete_banner(id_):
    b = Banner.query.filter_by(id=id_).first()
    if b:
        db.session.delete(b)
