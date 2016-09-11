# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file, get_biai_conf, set_biai_conf

@adminbp.route('/setting', methods=['GET', 'POST', ])
@login_required
def setting():
    if request.method == 'GET':

        site_name = get_biai_conf('site_info', 'site_name')
        site_domain = get_biai_conf('site_info', 'site_domain')
        site_filing_num = get_biai_conf('site_info', 'site_filing_num')
        site_locale = get_biai_conf('site_info', 'site_locale')

        company_name = get_biai_conf('site_content', 'company_name')
        service_phone = get_biai_conf('site_content', 'service_phone')
        company_location = get_biai_conf('site_content', 'company_location')

        return admin_response('setting.html',

                site_name=site_name,
                site_domain=site_domain,
                site_filing_num=site_filing_num,
                site_locale=site_locale,
                
                company_name=company_name,
                service_phone=service_phone,
                company_location=company_location,

                )
    elif request.method == 'POST':
        from ...form.admin import USettingForm 
        form = USettingForm()
        if not form.validate():
            return admin_response(
                    ret=-1,
                    msg='input error: ' + str(form.errors),
                    )

        site_name = form.site_name.data
        site_domain = form.site_domain.data
        site_filing_num = form.site_filing_num.data
        site_locale = form.site_locale.data

        company_name = form.company_name.data
        service_phone = form.service_phone.data
        company_location = form.company_location.data

        set_biai_conf('site_info', 'site_name', site_name)
        set_biai_conf('site_info', 'site_domain', site_domain)
        set_biai_conf('site_info', 'site_filing_num', site_filing_num)
        set_biai_conf('site_info', 'site_locale', site_locale)

        set_biai_conf('site_content', 'company_name', company_name)
        set_biai_conf('site_content', 'service_phone', service_phone)
        set_biai_conf('site_content', 'company_location', company_location)

        return admin_response(ret=0)


