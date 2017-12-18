import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    Testing = False
    CSRF_ENABLED = True
    SECRET_KEY = 'thisissecret'
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