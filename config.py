"""
    Details: Basic Config file setup
    Author: praveenjp
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    Testing = False
    CSRF_ENABLED = True
    SECRET_KEY = ';\x85\x0fd\x05\x96\xbf6`7nj\xb3\xc0U\xafF\xc5tL\xfdN\x93\xc8'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    Testing = True
