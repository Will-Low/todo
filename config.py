class Config(object):
    """
    Common configurations across all environments
    """

class DevelopmentConfig(config):
    """ 
    Configurations for development
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Configurations for production
    """

    DEBUG = False

app_config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
}
