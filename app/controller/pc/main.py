# -*- coding: utf-8 -*-
from . import pcbp 

from flask import render_template, request
from ...util.common import logger

@pcbp.route('/main/')
def index():
    logger.error('hayespantest')
    return render_template('pc/main_page.html')
