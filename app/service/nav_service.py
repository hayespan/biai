# -*- coding: utf-8 -*-

from flask import request
from ..model.nav import Nav

def get_navs():
    navs = Nav.query.all()
    nav_dict = {}
    for nav in navs:
        nav_dict[nav.meta_name] = nav
    return nav_dict

def get_nav_by_meta_name(meta_name):
    return Nav.query.filter_by(meta_name=meta_name).first()

