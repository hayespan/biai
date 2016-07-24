# -*- coding: utf-8 -*-
from flask import render_template, request, abort, url_for, session

from . import pcbp 
from ..base_func import *
from ...util.common import logger, json_response, get_now_timestamp

@pcbp.route('/join_us', methods=['GET', ])
def join_us():
    pass

@pcbp.route('/join_us/cooperation/post', methods=['POST', ])
def cooperation_post():
    pass
