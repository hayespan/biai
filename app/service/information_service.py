# -*- coding: utf-8 -*-

from .. import db
from ..model.information import Information 

def get_information_list():
    return Information.query.order_by(db.desc('weight'))\
            .order_by(db.desc('id')).all()

def create_information(title, weight, news):
    i = Information(
            title=title,
            weight=weight,
            news_id=news.id,
            )
    db.session.add(i)
    db.session.commit()
    return 0, i.id

def delete_information(id_):
    i = Information.query.filter_by(id=id_).first()
    if i:
        db.session.delete(i)

