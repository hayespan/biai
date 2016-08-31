# -*- coding: utf-8 -*-
import random

from . import pcbp 

from flask import render_template, request, abort, url_for, session

from ..base_func import *
from ...util.common import logger, json_response, get_now_timestamp
from ...service import banner_service
from ...service import product_category_service
from ...service import video_service
from ...service import consult_service
from ...service import product_service
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
    succ = send_sms(form.mobile.data, '您的验证码是：%s，有效期为%d分钟' % (code, valid_delta, ))
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
    code = session.get('captcha_mobile_code', '')
    expire = session.get('captcha_mobile_expire', 0)
    correct = code == form.code.data and expire>get_now_timestamp()
    return response(ret=0, correct=correct)


@pcbp.route('/set_locale/<string:lang>', methods=['GET', ])
def set_locale(lang):
    if lang in ('zh_CN', 'en_US', ):
        session['locale'] = lang
    elif session.get('locale', None):
        del session['locale']
    return response(ret=0)

