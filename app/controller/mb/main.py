# -*- coding: utf-8 -*-
from . import mbbp 

from flask import render_template, request

@mbbp.route('/main/')
def index():
    return render_template('mb/main_page.html')
