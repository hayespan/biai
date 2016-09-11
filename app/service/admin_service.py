# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import request
import datetime
from .. import db
from ..model.admin import Admin 

def get_admins():
    return Admin.query.all()

def create_admin(username, password, real_name):
    ad = Admin(
            username=username,
            real_name=real_name,
            is_admin=True,
            )
    ad.set_password(password)
    db.session.add(ad)
    db.session.commit()
    return 0, ad.id

def delete_admin(id_):
    ad = Admin.query.filter_by(id=id_).first()
    if ad:
        db.session.delete(ad)

def fresh_login_info(admin):
    admin.last_login = datetime.datetime.now()
    admin.last_login_ip = request.remote_addr
    db.session.add(admin)

