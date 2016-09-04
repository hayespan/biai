# coding=utf-8
import os
from .. import db
import socket
import datetime
from ..model.admin_system_setting import WebsiteSetting, AdminSetting
from files_service import fileManager
from werkzeug.utils import secure_filename


class SysSettingManager(object):
    def __init__(self):
        self.classify_path = '/static/img/classify'
        self.admin_lists = {
            'website': WebsiteSetting,
            'admin': AdminSetting,
        }

    def get_data(self, ):
        data = {
            'website': WebsiteSetting.query.all(),
            'admin': AdminSetting.query.all(),
        }
        return data

    @staticmethod
    def init_data():
        website_content = [
            ('比爱网', 'www.biai.com', '123456'),

        ]
        admin_content = [
            ('u1', 'p1', '张三', '123.57.81.70', '2016-08-25 12:06', '2016-07-22 11:06'),
            ('u2', 'p2', '李四', '123.57.82.70', '2016-08-26 13:06', '2016-07-23 12:06'),
            ('u3', 'p3', '王五', '123.57.83.70', '2016-08-27 14:06', '2016-07-24 13:06'),
        ]
        for each in website_content:
            if WebsiteSetting.query.filter_by(name=each[0]).count() == 0:
                item = WebsiteSetting(each[0], each[1], each[2])
                db.session.add(item)
        for each in admin_content:
            if AdminSetting.query.filter_by(username=each[0]).count() == 0:
                item = AdminSetting(each[0], each[1], each[2], each[3], each[4], each[5])
                db.session.add(item)
        db.session.commit()

    def change_website(self, request):
        data = request.form
        item = self.admin_lists['website'].query.first()
        item.name = data['name']
        item.url = data['url']
        item.num = data['num']
        db.session.commit()

    def add_admin(self, request):
        data = request.form
        admin = self.admin_lists['admin']
        item = admin(data['username'], data['password'], data['true_name'],
                     'x.x.x.x', 'xxxx-xx-xx xx:xx', str(datetime.datetime.now())[:16])
        db.session.add(item)
        db.session.commit()

    def change_admin(self, username):
        host_name = socket.getfqdn(socket.gethostname())
        host_addr = socket.gethostbyname(host_name)
        admin = self.admin_lists['admin']
        item = admin.query.filter_by(username=username).first()
        item.ip = host_addr
        item.login_time = str(datetime.datetime.now())[:16]
        db.session.commit()

    def del_admin(self, id_):
        admin = self.admin_lists['admin']
        item = admin.query.filter_by(id=id_).first()
        if str(item) != 'None':
            db.session.delete(item)
            db.session.commit()

sysSettingManager = SysSettingManager()
