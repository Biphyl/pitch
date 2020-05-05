# import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# class Config():

    
#     SECRET_KEY = '435313ea80b5a872114356a1'
#     # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://biron:Biron4745@localhost/pitches'
#     UPLOADED_PHOTOS_DEST ='app/static/photos'
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 465
#     MAIL_USE_TLS = False
#     MAIL_USE_SSL = True
#     MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#     MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
#     SUBJECT_PREFIX = 'Pitches'
# class ProductionConfig(Config):
#      pass
# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
# class DevelopmentConfig(Config):
#     # DEVELOPMENT = True
#     DEBUG = True
# class TestingConfig(Config):
#     TESTING = True
# config_options = {
# 'test':TestingConfig,
# 'development':DevelopmentConfig
# }

import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'Bilovine'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'bironodhiambo00@gmail.com@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/pitch'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}