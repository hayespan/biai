#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import App
app = App()
realapp = app.app

if __name__ == '__main__':
    realapp.run(host='0.0.0.0')
