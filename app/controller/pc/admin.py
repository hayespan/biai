# -*- coding: utf-8 -*-
from . import pcbp

from flask import render_template, request, abort, url_for

from ..base_func import *
from ...service.home_service import homeManager
from ...service.join_us_service import joinUsManager
from ...service.sys_setting_service import sysSettingManager
from ...service.files_service import fileManager


@pcbp.route('/admin', methods=['GET', ])
def admin():
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home', methods=['GET', ])
def admin_home():
    return response_home_data('admin/home.html')


@pcbp.route('/admin/join', methods=['GET', ])
def admin_join():
    return response_join_data('admin/join_us.html')


@pcbp.route('/admin/sys', methods=['GET', ])
def admin_sys():
    return response_sys_data('admin/sys_setting.html')


@pcbp.route('/admin/home/add_video', methods=['POST'])
def admin_home_video():
    homeManager.add_video(request)
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home/add_poster', methods=['POST'])
def admin_home_poster_add():
    homeManager.add_poster(request)
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home/del_poster', methods=['POST'])
def admin_home_poster_del():
    id_ = request.json['id']
    homeManager.delete(id_, 'poster')
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home/del_video', methods=['POST'])
def admin_home_video_del():
    id_ = request.json['id']
    homeManager.delete(id_, 'video')
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home/hide_new', methods=['POST'])
def admin_home_hide_new():
    id_ = request.json['id']
    homeManager.hide_new(int(id_))
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home/show_new', methods=['POST'])
def admin_home_show_new():
    id_ = request.json['id']
    homeManager.show_new(int(id_))
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home/change_new', methods=['POST'])
def admin_home_change_new():
    homeManager.change_new(request.json)
    return response_home_data('admin/home.html')


@pcbp.route('/admin/home/change_classify', methods=['POST'])
def admin_home_classify():
    homeManager.change_classify(request)
    return response_home_data('admin/home.html')


@pcbp.route('/admin/<string:type_>/<string:part>/download/<string:name>', methods=['GET'])
def admin_download(type_, part, name):
    return fileManager.download(type_, part, name)


@pcbp.route('/admin/join/add/<string:part>', methods=['POST'])
def admin_join_add(part):
    if part == 'participate':
        joinUsManager.add_participate(request)
    else:
        joinUsManager.add_hiring(request)
    return response_join_data('admin/join_us.html')


@pcbp.route('/admin/sys/add', methods=['POST'])
def admin_sys_add():
    sysSettingManager.add_admin(request)
    return response_sys_data('admin/sys_setting.html')


@pcbp.route('/admin/sys/change', methods=['POST'])
def admin_sys_change():
    sysSettingManager.change_website(request)
    return response_sys_data('admin/sys_setting.html')


@pcbp.route('/admin/sys/login', methods=['POST'])
def admin_sys_login():
    sysSettingManager.change_admin(request.form['username'])
    return response_sys_data('admin/sys_setting.html')


@pcbp.route('/admin/sys/del/<int:id_>', methods=['POST'])
def admin_sys_del(id_):
    sysSettingManager.del_admin(id_)
    return response_sys_data('admin/sys_setting.html')


def response_home_data(path):
    return response(path,
                    data=homeManager.get_data(),
                    title='Admin')


def response_join_data(path):
    return response(path,
                    data=joinUsManager.get_data(),
                    title='Admin')


def response_sys_data(path):
    return response(path,
                    data=sysSettingManager.get_data(),
                    title='Admin')
