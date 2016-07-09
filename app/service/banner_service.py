# -*- coding: utf-8 -*-

from .. import db
from ..model.banner import Banner

def get_banners():
    return Banner.query.order_by(db.desc('weight'))\
            .order_by(db.desc('id')).all()
