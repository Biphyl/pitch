import os


class Config():









class ProductionConfig(config):
    pass

class StagingConfig(config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(config):
    DEBUG = True

    
