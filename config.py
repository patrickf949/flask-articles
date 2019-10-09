  
"""
module config to configure database
"""
class Config:
    """
    parent config class
    """
    DEBUG = False
    dbname = "karibu"

class DevelopmentConfig(Config):
    """
    class for development configuration
    """
    DEBUG = True

class TestingConfig(Config):
    """
    class for testing configuration
    """
    DEBUG = False
    TESTING = True

class ProductionConfig(Config):
    """ production config class """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
