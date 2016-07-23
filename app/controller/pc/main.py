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
    return response('pc/search_product_list.html',
            product_list=product_list,
            key=key,
            )

@pcbp.route('/')
def index():
    banner_list = banner_service.get_banners()
    product_category_list = product_category_service.get_categories()
    video_list = video_service.get_videos()
    consult_page_content = consult_service.get_page_content()
    return response('pc/main_page.html', 
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
    session['captcha_mobile'] = randi
    session['captcha_mobile_expire'] = get_now_timestamp() + valid_delta*60
    succ = send_sms(form.mobile.data, '您的验证码是：%s，有效期为%d分钟' % (code, valid_delta, ))
    response(
            ret=1-succ,
            msg='send fail' if not succ else 'send succ',
            )

