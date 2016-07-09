# -*- coding: utf-8 -*-

from ..model.nav import Nav

def get_navs():
    navs = Nav.query.all()
    nav_dict = {}
    for nav in navs:
        nav_dict[nav.meta_name] = nav
    return nav_dict

