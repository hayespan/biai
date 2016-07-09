# -*- coding: utf-8 -*-

from .. import db
from ..model.video import Video 

def get_videos():
    return Video.query.order_by(db.desc('weight'))\
            .order_by(db.desc('id')).all()
