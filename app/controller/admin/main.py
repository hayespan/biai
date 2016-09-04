# -*- coding: utf-8 -*-
import os
import re
import json
import datetime
from hashlib import sha1

from flask import render_template, request, redirect, flash, url_for, session, jsonify, abort
from flask.ext.login import login_required, login_user, logout_user, current_user

from . import adminbp 
from ...model.admin import Admin

@adminbp.route('/login', methods=['GET','POST'])
def login():
    from ...form.admin import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is not None and admin.verify_password(form.password.data):
            login_user(admin, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('admin.login'))
        flash('Invalid username or password')
    return render_template('pc/admin/login.html')

@adminbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@adminbp.route('/login_required', methods=['GET'])
@login_required
def test_login_required():
    return 'secret'

