# -*- coding: utf-8 -*-
import time
import os
import datetime 
from flask import jsonify, request, redirect, current_app
from functools import wraps
from hashlib import md5

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

def get_now_timestamp():
    return datetime_2_unixstamp(datetime.datetime.now())

SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/../static/')
def save_form_file(file_, subpath=None, filename_=None):
    '''
    save pic data and return file object
    '''
    full_path = os.path.join(SAVE_PATH, subpath) if subpath is not None else SAVE_PATH
    try:
        if filename_ is None:
            fm = file_.filename.rsplit('.', 1)[1]
            filename = md5(os.urandom(64)).hexdigest()+'.'+fm
        else:
            filename = filename_
        file_.save('%s/%s' % (full_path, filename))
    except Exception, e:
        logger.error('save file fail, exception: ' + e.message)
        return (False, None, ) 
    return (True, filename)

def remove_file(subpath, filename):
    '''
    remove file
    '''
    full_path = os.path.join(SAVE_PATH, subpath, filename)
    try:
        os.remove(full_path)
    except Exception, e:
        logger.error('remove file fail, exception: ' + e.message)
        return (False, full_path)
    return (True, full_path)

