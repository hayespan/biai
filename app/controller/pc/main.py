# -*- coding: utf-8 -*-
import random

from . import pcbp 

from flask import render_template, request, abort, url_for, session, redirect
from flask.ext.babel import gettext

from ..base_func import response
from ...util.common import logger, json_response, get_now_timestamp
from ...service import banner_service
from ...service import product_category_service
from ...service import video_service
from ...service import consult_service
from ...service import product_service
from ...service import captcha_service
from ...service import information_service
from ...util.sms import send_sms

@pcbp.route('/search', methods=['POST', ])
def search():
    from ...form.main import SearchForm
    form = SearchForm()
    key = ''
    if form.validate():
        key = form.key.data
    product_list = product_service.search_key(key)
    return response('search_product_list.html',
            product_list=product_list,
            key=key,
            )


@pcbp.route('/')
def index():
    banner_list = banner_service.get_banners()
    product_category_list = product_category_service.get_categories()
    video_list = video_service.get_videos()
    consult_page_content = consult_service.get_page_content()
    information_list = information_service.get_information_list()
    return response('main_page.html', 
            banner_list=banner_list,
            product_category_list=product_category_list,
            video_list=video_list,
            consult_page_content=consult_page_content,
            )


@pcbp.route('/captcha/mobile_trigger', methods=['POST', ])
def captcha_mobile_trigger():
    from ...form.main import MobileForm 
    form = MobileForm()
    if not form.validate():
        response(
                ret=-1,
                msg='invalid mobile'
                )
    valid_delta = 5
    randi = random.randint(0, 9999)
    code = '%04d' % randi
    session['captcha_mobile_code'] = randi
    session['captcha_mobile_expire'] = get_now_timestamp() + valid_delta*60
    s = __('hayes')
    succ = send_sms(form.mobile.data,
            gettext('您的验证码是：%(code)，有效期为%(valid_delta)分钟', 
                code=code,
                valid_delta=valid_delta, 
                )
            )
    return response(
            ret=1-succ,
            msg='send fail' if not succ else 'send succ',
            )


@pcbp.route('/captcha/mobile_check', methods=['POST', ])
def captcha_mobile_check():
    from ...form.main import CaptchaForm
    form = CaptchaForm()
    if not form.validate():
        return response(
                ret=-1,
                msg='captcha code format error',
                )
    correct = captcha_service.check_captcha(form.code.data)
    return response(ret=0, correct=correct)


@pcbp.route('/set_locale/<string:lang>', methods=['GET', ])
def set_locale(lang):
    if lang in ('zh_CN', 'en_US', ):
        session['locale'] = lang
    elif session.get('locale', None):
        del session['locale']
    return redirect(url_for('pc.index'))

