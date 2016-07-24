#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import App, db
app = App()

def create_default_nav():
    from app.model.nav import Nav
    nav_meta_names = [
            ('about', '关于比爱', ),
            ('shop', '官方商城', ), 
            ('contact', '联系我们', ),
            ]
    for i in nav_meta_names:
        if Nav.query.filter_by(meta_name=i[0]).count() == 0:
            about_nav = Nav(
                    meta_name=i[0],
                    title=i[1],
                    )
            from app.model.simple_nav_page import SimpleNavPage
            page = SimpleNavPage(
                    content='empty',
                    )
            about_nav.simple_nav_page = page
            db.session.add(about_nav)
    db.session.commit()

with app.app.app_context():
    db.create_all()

    create_default_nav()
