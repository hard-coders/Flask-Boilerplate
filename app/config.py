class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = 'dev'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SECRET_KEY = 'test'


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SECRET_KEY = 'prod'
