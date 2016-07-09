# -*- coding: utf-8 -*-
import time
import datetime 
from flask import jsonify, request, redirect, current_app
from functools import wraps

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(self, *args, **kwargs)
    def __getattr__(self, name):
        return self[name];
    def __setattr__(self, name, value):
        assert isinstance(name, str) and isinstance(value, int) 
        self[name] = value
        self[value] = name

# logger used during request
class RequestLogger(object):
    def __init__(self):
        self.logger = None

    def __getattr__(self, attrname):
        if self.logger is None:
            self.logger = current_app.logger
        return getattr(self.logger, attrname)
logger = RequestLogger()

def json_error(ERROR):
    return jsonify({'code': ERROR[0], 'data': ERROR[1]})

def json_response(**data):
    return jsonify({'code': 0, 'data': data})

USERAGENT = ('micromessenger', 'Mobile', 'iPhone', 'Windows Phone', 'UCWEB', 'Fennec', 'Opera Mobi', 'BlackBerry', )

def via_mobile():
    s = request.headers.get('User-Agent')
    if s is None:
        return False
    for i in USERAGENT:
        if i in s:
            return True
    return False

def PC_MB_distribute(url):
    '''pc and mobile end distribution'''
    def _PC_MB_distribute(func):
        @wraps(func) 
        def _wrap(*args, **kwargs):
            if viaMobile():
                return redirect(url)
            return func(*args, **kwargs)
        return _wrap
    return _PC_MB_distribute

def datetime_2_unixstamp(dt):
    '''datetime obj parsed to unixstamp
    '''
    return time.mktime(dt.timetuple())

def timedelta_2_second(hours_f):
    '''floating type, hour-delta, parsed to seconds
    '''
    return datetime.timedelta(hours=float(hours_f)).seconds
