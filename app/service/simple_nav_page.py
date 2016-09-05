# -*- coding: utf-8 -*-

import datetime

from flask import request
from ..model.simple_nav_page import SimpleNavPage
from .. import db

def update_simple_nav_page(id_, content):
    snp = SimpleNavPage.query.filter_by(id=id_).first()
    if not snp:
        return -1
    snp.content = content
    snp.modify_time = datetime.datetime.now()
    db.session.add(snp)
    return 0
