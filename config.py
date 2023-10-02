class BaseConfig():
    'Base config class'
    SECRET_KEY = 'random secret'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VAR = 'moja wartość'

class ProductionConfig(BaseConfig):
    'Specs production'
    DEBUG = False
    # SECRET_KEY = open('').read()

class StagingConfig(BaseConfig):
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    SECRET_KEY = "another key"
    TESTING = True