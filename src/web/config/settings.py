from enum import Enum
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class ValidEnvironments(Enum):
    """Enum to control valid environment config inputs"""
    Development = 'Development',
    Test = 'Test',
    Production = 'Production'


class Default:
    """Default Configuration that all environments will default to"""
    APP_NAME = "app"
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "A0Zr98jyX RHH!jmN]LWX/,?RT"
    ENV = os.environ.get("ENV") or ValidEnvironments.Development
    SERVER = os.environ.get("SERVER") or 'localhost'

    SQLALCHEMY_DATABASE_URI = "postgresql://admin:password@postgres:5432/portdb"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Default):
    """Development environment"""
    DEBUG = False
    TESTING = True
    ENV = os.environ.get("ENV") or ValidEnvironments.Development
    SERVER = os.environ.get("SERVER") or "egu-nyc-dev-001"
   
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Test(Default):
    """Continuous Integration (CI) / User Acceptance"""
    DEBUG = False
    TESTING = True
    ENV = os.environ.get("ENV") or ValidEnvironments.Test
    SERVER = os.environ.get("SERVER") or "egu-nyc-dev-001"

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Production(Default):
    """Production"""
    DEBUG = False
    TESTING = False
    ENV = os.environ.get("ENV") or ValidEnvironments.Production
    SERVER = os.environ.get("SERVER") or "egu-nyc-prd-001"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
