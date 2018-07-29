#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "HuChong"
# Date: 2018/4/22

from flask import Blueprint

home = Blueprint('home', __name__, static_folder='./static')

import app.home.views
