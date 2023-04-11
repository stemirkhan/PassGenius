import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SECRET_KEY = 'djkflsgbnkjdgn'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = False
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    DEBUG = False
