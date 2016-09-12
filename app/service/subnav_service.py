# -*- coding: utf-8 -*-

from flask import request
from ..model.subnav import SubNav
from . import nav_service
from .. import db

def read_subnav(id_):
    subnav = SubNav.query.filter_by(id=id_).first()
    return subnav

def create_subnav(nav_id_, title, link):
    nav = nav_service.read_nav(nav_id_)
    if not nav:
        return -1
    subnav = SubNav(
            title=title,
            link=link,
            nav_id=nav.id,
            )
    db.session.add(subnav)
    db.session.commit()
    return 0, subnav.id

def delete_subnav(id_):
    subnav = SubNav.query.filter_by(id=id_).first()
    if subnav:
        db.session.delete(subnav)

