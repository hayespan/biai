#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import App, db
app = App()

def create_default_nav():
    from app.model.nav import Nav
    nav_meta_names = [
            ('about', '关于比爱', '/about'),
            ('shop', '官方商城', '/shop'), 
            ('contact', '联系我们', '/contact'),
            ]
    for i in nav_meta_names:
        if Nav.query.filter_by(meta_name=i[0]).count() == 0:
            about_nav = Nav(
                    meta_name=i[0],
                    title=i[1],
                    link=i[2],
                    )
            from app.model.simple_nav_page import SimpleNavPage
            page = SimpleNavPage(
                    content='empty',
                    )
            about_nav.simple_nav_page = page
            db.session.add(about_nav)
        if i[0] == 'shop':
            shop_nav = Nav.query.filter_by(meta_name=i[0]).first()
            if shop_nav and not shop_nav.subnavs:
                from app.model.subnav import SubNav
                sn1 = SubNav(
                        title='1688官网',
                        nav=shop_nav,
                        link='www.baidu.com',
                        )
                sn2 = SubNav(
                        title='比爱企业店',
                        nav=shop_nav,
                        link='cn.bing.com',
                        )
                db.session.add(sn1)
                db.session.add(sn2)


    db.session.commit()

with app.app.app_context():
    db.create_all()

    create_default_nav()

