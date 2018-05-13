#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "HuChong"
# Date: 2018/4/22

from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.views
