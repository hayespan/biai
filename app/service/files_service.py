# coding=utf-8
import os
from flask import current_app, send_file, make_response


class FilesManager(object):
    def __init__(self):
        pass

    def change_file(self, f, name, old_name):
        old_file = old_name
        self.delete_old_file(old_file)
        abs_path = os.path.join(current_app.static_folder, 'img/home/classify/', name)
        f.save(abs_path)

    @staticmethod
    def add_file(f, name, kind):
        if kind == 'poster':
            abs_path = os.path.join(current_app.static_folder, 'img/home/poster/', name)
        elif kind == 'video':
            new_file = 'mainpage/' + name
            abs_path = os.path.join(current_app.static_folder, 'video', new_file)
        else:
            abs_path = os.path.join(current_app.static_folder,
                                    'img/join_us/' + kind + '/', name)
        f.save(abs_path)

    @staticmethod
    def download(type_, part, name):
        response = make_response(send_file("static/img/" + type_ + '/' + part + '/' + name))
        response.headers["Content-Disposition"] = "attachment; filename=" + name
        return response

    @staticmethod
    def delete_file(name, kind):
        if kind == 'poster':
            abs_path = os.path.join(current_app.static_folder, 'img/home/' + kind + '/', name)
        else:
            abs_path = os.path.join(current_app.static_folder, 'video/mainpage/', name)
        os.remove(abs_path)

    @staticmethod
    def delete_old_file(old_file):
        if os.path.exists(old_file):
            os.remove(old_file)


fileManager = FilesManager()

