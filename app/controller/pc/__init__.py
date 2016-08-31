# -*- coding: utf-8 -*-
from flask import Blueprint

pcbp = Blueprint(
        'pc',
        __name__,
        # if templates & static dirs are in
        # subapp/ then the following configs
        # are needed.
        # template_folder='templates',
        # static_folder='static'.
        )

from . import main
from . import news
from . import about
from . import creativity
from . import product
from . import shop
from . import contact
from . import join_us
from . import ueditor
from . import admin
