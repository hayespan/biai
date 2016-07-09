# -*- coding: utf-8 -*-

import os
from flask import current_app

consult_page_filename = 'consult_page'

def get_page_content():
    abs_path = os.path.join(current_app.static_folder, 'page', consult_page_filename)
    content = ''
    with open(abs_path, 'r') as f:
        content = f.read()
    return content

