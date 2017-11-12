class BaseConfig:
    """docstring for BaseConfig."""
    """   Base Configuration    """
    DEBUG   = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """docstring for DevelopmentConfig."""
    DEBUG = True

class TestingConfig(BaseConfig):
    """docstring for TestingConfig."""
    DEBUG   = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """docstring for ProductionConfig."""
    DEBUG = False
