# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .. import db
from ..model.video import Video 

def get_videos():
    return Video.query.order_by(db.desc('weight'))\
            .order_by(db.desc('id')).all()

def create_video(weight, name, pic_file_id, video_file_id):
    v = Video(
            weight=weight,
            name=name,
            pic_id=pic_file_id,
            file_id=video_file_id,
            )
    db.session.add(v)
    db.session.commit()
    return 0, v.id

def delete_video(id_):
    v = Video.query.filter_by(id=id_).first()
    if v:
        db.session.delete(v)

