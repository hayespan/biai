# -*- coding: utf-8 -*-

from flask import request
from ..model.nav import Nav
from .. import db

def get_navs():
    navs = Nav.query.all()
    nav_dict = {}
    for nav in navs:
        nav_dict[nav.meta_name] = nav
    return nav_dict

def get_nav_by_meta_name(meta_name):
    return Nav.query.filter_by(meta_name=meta_name).first()

def read_nav(id_):
    nav = Nav.query.filter_by(id=id_).first()
    return nav

def update_nav(id_, title, link):
    nav = read_nav(id_)
    if not nav:
        return -1
    nav.title = title
    nav.link = link
    db.session.add(nav)
    return 0

