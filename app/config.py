#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:huchong
import os
import redis


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1/movie?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 2
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1

    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
    FC_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")



class ProductionConfig(BaseConfig):
    SESSION_REDIS = redis.Redis(host='192.168.200.128', port=6379)  # 用于连接redis的配置


class DevelopmentConfig(BaseConfig):
    DEBUG =True
    SESSION_REDIS = redis.Redis(host='192.168.200.128', port=6379)  # 用于连接redis的配置


class TestingConfig(BaseConfig):
    SESSION_REDIS = redis.Redis(host='192.168.200.128', port=6379)  # 用于连接redis的配置


if __name__ == '__main__':
    pass
