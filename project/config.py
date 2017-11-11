class BaseConfig:
    """docstring for BaseConfig."""
    """   Base Configuration    """
    DEBUG   = False
    TESTING = False

class DevelopmentConfig:
    """docstring for DevelopmentConfig."""
    DEBUG = True

class TestingConfig:
    """docstring for TestingConfig."""
    DEBUG   = True
    TESTING = True

class ProductionConfig(object):
    """docstring for ProductionConfig."""
    DEBUG = False
