# -*- coding: utf-8 -*-
from flask import Blueprint

mbbp = Blueprint(
        'mb',
        __name__,
        # if templates & static dirs are in
        # subapp/ then the following configs
        # are needed.
        # template_folder='templates',
        # static_folder='static'.
        )

from . import main

