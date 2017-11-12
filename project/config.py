class BaseConfig:
    """docstring for BaseConfig."""
    """   Base Configuration    """
    DEBUG                          = False
    TESTING                        = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """docstring for DevelopmentConfig."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

class TestingConfig(BaseConfig):
    """docstring for TestingConfig."""
    DEBUG   = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URI')


class ProductionConfig(BaseConfig):
    """docstring for ProductionConfig."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
