# -*- coding: utf-8 -*-

from .. import db
from ..model.cooperation import Cooperation 

def get_cooperations():
    return Cooperation.query.order_by(db.desc('id')).all()

def create_cooperation(name, mobile, zone, 
        shop_range, develop_plan, cooperation_intention):
    cp = Cooperation(
            name=name,
            mobile=mobile,
            zone=zone,
            shop_range=shop_range,
            develop_plan=develop_plan,
            cooperation_intention=cooperation_intention,
            )
    db.session.add(cp)
    db.session.commit()
    return 0, cp.id

def read_cooperation(id_):
    cp = Cooperation.query.filter_by(id=id_).first()
    return cp

def delete_cooperation(id_):
    cp = Cooperation.query.filter_by(id=id_).first()
    if cp: 
        db.session.delete(cp)
