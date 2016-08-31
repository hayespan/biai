# coding=utf-8
import os
from .. import db
from ..model.admin_home import ClassifyAdmin, PosterAdmin, VideoAdmin, NewsAdmin
from files_service import fileManager
from werkzeug.utils import secure_filename


class HomeManager(object):
    def __init__(self):
        self.classify_path = '/static/img/classify'
        self.admin_lists = {
            'classify': ClassifyAdmin,
            'poster': PosterAdmin,
            'video': VideoAdmin,
            'news': NewsAdmin
        }

    def get_data(self,):
        data = {
            'classify': ClassifyAdmin.query.all(),
            'poster': PosterAdmin.query.all(),
            'video': VideoAdmin.query.all(),
            'news': NewsAdmin.query.all()
        }
        return data

    @staticmethod
    def init_data():
        classify_content = [
            ('摇铃', 't1.png'),
            ('床铃', 't2.png'),
            ('健身架', 't3.png'),
            ('益智玩具', 't4.png'),
            ('其他', 't5.png')
        ]
        news_content = [
            ('新闻1', False), ('新闻2', False), ('新闻3', False),
            ('新闻4', False), ('新闻5', False), ('新闻6', False),
            ('新闻7', False), ('新闻8', False), ('新闻9', False)
        ]
        for each in classify_content:
            if ClassifyAdmin.query.filter_by(name=each[0]).count() == 0:
                item = ClassifyAdmin(each[0], each[1])
                db.session.add(item)
        for each in news_content:
            if NewsAdmin.query.filter_by(name=each[0]).count() == 0:
                item = NewsAdmin(each[0], each[1])
                db.session.add(item)
        db.session.commit()

    # 编辑或修改
    def edit(self, data, kind):
        admin = self.admin_lists[kind]
        item = admin.query.filter_by(id=data['id']).first()
        if str(item) != 'None':
            item.name = data['name']
        db.session.commit()

    # 根据id删除,同时删除文件
    def delete(self, id_, kind):
        admin = self.admin_lists[kind]
        item = admin.query.filter_by(id=id_).first()
        if kind == 'poster' or 'video':
            fileManager.delete_file(item.name, kind)
        if str(item) != 'None':
            db.session.delete(item)
        db.session.commit()

    # 不显示新闻
    def hide_new(self, id_):
        item = self.admin_lists['news'].query.filter_by(id=id_).first()
        if str(item) != 'None':
            item.hide = True
            db.session.commit()

    # 显示新闻
    def show_new(self, id_):
        item = self.admin_lists['news'].query.filter_by(id=id_).first()
        if str(item) != 'None':
            item.hide = False
            db.session.commit()

    def change_new(self, data):
        item = self.admin_lists['news'].query.filter_by(id=data['id']).first()
        if str(item) != 'None':
            item.name = data['name']
            db.session.commit()

    # 分类管理
    def change_classify(self, request):
        f = request.files['classify']
        id_ = request.form['id']
        admin = self.admin_lists['classify']
        item = admin.query.filter_by(id=id_).first()
        if str(item) != 'None':
            old_name = item.img
            item.name = request.form['name']
            item.img = secure_filename(f.filename)
            db.session.commit()
            fileManager.change_file(f, item.img, old_name)

    # 添加视频
    def add_video(self, request):
        f = request.files['video']
        name = secure_filename(f.filename)
        admin = self.admin_lists['video']
        item = admin(name)
        db.session.add(item)
        db.session.commit()
        fileManager.add_file(f, name, 'video')

    # 添加海报
    def add_poster(self, request):
        f = request.files['poster']
        name = secure_filename(f.filename)
        admin = self.admin_lists['poster']
        item = admin(name, name)
        db.session.add(item)
        db.session.commit()
        fileManager.add_file(f, name, 'poster')


homeManager = HomeManager()

