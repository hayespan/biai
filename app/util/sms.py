# -*- coding: utf-8 -*-
import requests
from common import logger
from flask import current_app

def send_sms(mobile_list, content):
    mobiles = None
    if isinstance(mobile_list, unicode) or \
            isinstance(mobile_list, str):
        mobiles = mobile_list
    else:
        mobiles = ','.join(mobile_list)
    if not mobiles or not content:
        return None
    if current_app.config['SMS_FAKE']:
        return True 
    logger.info('mobile: ' + mobiles)
    try:
        resp = requests.post(current_app.config['SMS_ADDR'],
                data={
                    'name': current_app.config['SMS_USERNAME'],
                    'pwd': current_app.config['SMS_PASSWORD'],
                    'content': content,
                    'mobile': mobiles,
                    'sign': current_app.config['SMS_SIGN'],
                    'type': 'pt',
                    },
                timeout=5)
    except Exception, e:
        logger.error(e.message)
        return False
    logger.info(resp.status_code)
    logger.info(resp.text) 
    if resp.status_code != 200:
        return False
    rsp_list = resp.text.split(',')
    ret_code = int(rsp_list[0])
    return ret_code == 0 

