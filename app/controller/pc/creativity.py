# -*- coding: utf-8 -*-
from . import pcbp 

from flask import render_template, request, abort, url_for

from ..base_func import *
from ...util.common import logger, json_response

@pcbp.route('/creativity')
def creativity():
    return response('pc/creativity.html')

# @pcbp.route('/creativity/post')
