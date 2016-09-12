# -*- coding: utf-8 -*-
from . import adminbp 

from flask import render_template, request, abort, url_for
from flask.ext.login import login_required, current_user

from ..base_func import admin_response
from ...util.common import logger, json_response, save_form_file
from ...service import video_service 
from ...model.video import Video 

@adminbp.route('/video')
# @login_required
def l_video():
    video_list= video_service.get_videos()
    return admin_response('video_list.html',
            video_list=video_list,
            )

@adminbp.route('/video/create', methods=['POST', ])
# @login_required
def cu_video():
    from ...form.admin import CVideoForm 
    form = CVideoForm()
    if not form.validate():
        return admin_response(
                ret=-1,
                msg='input error: ' + str(form.errors),
                )
    weight = form.weight.data or 0
    name = form.name.data or ''
    succ, pic_file_id = save_form_file(form.pic.data, 
            Video.get_pic_dir())
    if not succ:
        return admin_response(
                ret=-2,
                msg='save video img fail.',
                )
    succ, video_file_id = save_form_file(form.video.data, 
            Video.get_file_dir())
    if not succ:
        return admin_response(
                ret=-2,
                msg='save video file fail.',
                )
    ret, new_id = video_service.create_video(
            weight, name, pic_file_id, video_file_id, 
            )
    return admin_response(ret=ret, id=new_id)


@adminbp.route('/video/delete', methods=['POST', ])
# @login_required
def d_video():
    from ...form.admin import DVideoForm 
    form = DVideoForm()
    if not form.validate():
        return admin_response(
                id=-1,
                msg='input error: ' + str(form.errors),
                )
    id_ = form.id.data
    video_service.delete_video(id_)
    return admin_response(ret=0)

