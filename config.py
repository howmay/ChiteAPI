# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    MONGODB_SETTINGS = {
        'db': 'chite',
        'host': 'mongodb://python-stock:bNMbTAddsZEwpVRI@amazondata-shard-00-00-7op9t.gcp.mongodb.net:27017,amazondata-shard-00-01-7op9t.gcp.mongodb.net:27017,amazondata-shard-00-02-7op9t.gcp.mongodb.net:27017/chite?ssl=true&replicaSet=AmazonData-shard-0&authSource=admin&retryWrites=true&w=majority'
    }


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
