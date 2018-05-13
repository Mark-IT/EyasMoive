#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "HuChong"
# Date: 2018/4/22

from flask import Flask


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint


from .ext import *  #导入组件
from .models import * # 导入models中的表，不然数据库迁移无效


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'sdiusdfsdf'
    # 设置配置文件
    app.config.from_object('app.config.DevelopmentConfig')

    # 初始化扩展插件
    db.init_app(app)

    # 这里注册你的中间件
    """
    @app.before_first_request
    def _before_first_request():
        pass
    """

    # 注册蓝图

    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    return app
