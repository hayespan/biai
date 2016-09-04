# coding=utf-8
import os
from .. import db
from ..model.admin_join_us import ParticipateAdmin, HiringAdmin
from files_service import fileManager
from werkzeug.utils import secure_filename


class JoinUsManager(object):
    def __init__(self):
        self.classify_path = '/static/img/classify'
        self.admin_lists = {
            'participate': ParticipateAdmin,
            'hiring': HiringAdmin,
        }

    def get_data(self, ):
        data = {
            'participate': ParticipateAdmin.query.all(),
            'hiring': HiringAdmin.query.all(),
        }
        return data

    @staticmethod
    def init_data():
        participate_content = [
            ('张三', '15521294098', 'p1.png'),
            ('李四', '15521294092', 'p2.png'),
            ('王五', '15521294090', 'p3.png'),
        ]
        hiring_content = [
            ('张五', '服务员', '15521294098', 'p1.png'),
            ('李四', '老师', '15521294098', 'p2.png'),
            ('王三', '清洁工', '15521294098', 'p3.png'),
        ]
        for each in participate_content:
            if ParticipateAdmin.query.filter_by(name=each[0]).count() == 0:
                item = ParticipateAdmin(each[0], each[1], each[2])
                db.session.add(item)
        for each in hiring_content:
            if HiringAdmin.query.filter_by(name=each[0]).count() == 0:
                item = HiringAdmin(each[0], each[1], each[2], each[3])
                db.session.add(item)
        db.session.commit()

    def add_participate(self, request):
        data = request.form
        f = request.files['file']
        admin = self.admin_lists['participate']
        filename = secure_filename(f.filename)
        item = admin(data['name'], data['contact'], filename)
        db.session.add(item)
        db.session.commit()
        fileManager.add_file(f, filename, 'participate')

    def add_hiring(self, request):
        data = request.form
        f = request.files['file']
        admin = self.admin_lists['hiring']
        filename = secure_filename(f.filename)
        item = admin(data['name'], data['job'], data['contact'],  filename)
        db.session.add(item)
        db.session.commit()
        fileManager.add_file(f, filename, 'hiring')


joinUsManager = JoinUsManager()
