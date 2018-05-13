#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "HuChong"
# Date: 2018/4/22



from . import home

@home.route('/')
def index():
    return