# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import nav_service 
from ...model.nav import Nav 

@adminbp.route('/nav')
#@login_required
def l_nav():
    main_nav = nav_service.get_nav_by_meta_name('main')
    about_nav = nav_service.get_nav_by_meta_name('about')
    news_nav = nav_service.get_nav_by_meta_name('news')
    product_nav = nav_service.get_nav_by_meta_name('product')
    creativity_nav = nav_service.get_nav_by_meta_name('creativity')
    join_us_nav = nav_service.get_nav_by_meta_name('join_us')
    shop_nav = nav_service.get_nav_by_meta_name('shop')
    contact_nav = nav_service.get_nav_by_meta_name('contact')
    return admin_response('nav.html',
            main_nav=main_nav,
            about_nav=about_nav,
            news_nav=news_nav,
            product_nav=product_nav,
            creativity_nav=creativity_nav,
            join_us_nav=join_us_nav,
            shop_nav=shop_nav,
            contact_nav=contact_nav,
            )

@adminbp.route('/nav/modify', methods=['POST', ])
#@login_required
def u_nav():
    from ...form.admin import UNavForm
    form = UNavForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    title = form.title.data 
    link = form.link.data
    nav_service.update_nav(id_, title, link)
    return admin_response(
            ret=0,
            )

