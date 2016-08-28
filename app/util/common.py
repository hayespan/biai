# -*- coding: utf-8 -*-
import time
import os
import math
import ConfigParser
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

def gen_random_filename(fmt=None):
    filename = md5(os.urandom(64)).hexdigest()
    if fmt:
        return filename + '.' + fmt
    return filename 

SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/')
def save_form_file(file_, subpath=None, filename_=None):
    '''
    save pic data and return file object
    '''
    full_path = os.path.join(SAVE_PATH, subpath) if subpath is not None else SAVE_PATH
    try:
        if filename_ is None:
            if isinstance(file_, bytes):
                return (False, None) 
            fmt = file_.filename.rsplit('.', 1)[1]
            filename = gen_random_filename(fmt)
        else:
            filename = filename_
        if isinstance(file_, bytes):
            with open(os.path.join(full_path, filename), 'wb') as _f:
                _f.write(file_)
        else:
            file_.save(os.path.join(full_path, filename))
    except Exception, e:
        logger.error('save file fail, exception: ' + str(e))
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

def page_info(tot, per, cur):
    return {
            'min': 1,
            'max': int(math.ceil(tot*1./per)) or 1, 
            'cur': cur,
            }

def page_limit(tot, per, cur):
    if tot == 0:
        return (0, 0)
    minpage = 1
    maxpage = int(math.ceil(tot*1./per))
    cur = max(minpage, cur)
    cur = min(maxpage, cur)
    idx = (cur-1)*per
    return (idx, per)

def get_biai_conf(sec, key, type_=str):
    try:
        BIAI_CONF_PATH = current_app.config['BIAI_CONFIG_PATH']
        cf = ConfigParser.ConfigParser()
        cf.read(BIAI_CONF_PATH)
        if type_ == str:
            result = cf.get(sec, key)
        elif type_ == int:
            result = cf.getint(sec, key)
        elif type_ == float:
            result = cf.getfloat(sec, key)
        elif type_ == bool:
            result = cf.getboolean(sec, key)
        else:
            logger.error('invalid read type: ' + str(type_))
            return False, None
        return True, result
    except Exception, e:
        logger.error('get_biai_conf exception: ' + str(e))
    return False, None

def set_biai_conf(sec, key, val):
    try:
        BIAI_CONF_PATH = current_app.config['BIAI_CONFIG_PATH']
        cf = ConfigParser.ConfigParser()
        cf.read(BIAI_CONF_PATH)
        cf.set(sec, key, val)
        with open(BIAI_CONF_PATH, 'w') as f_:
            cf.write(f_)
        return True
    except Exception, e:
        logger.error('set_biai_conf exception: ' + str(e))
    return False

