import os

from dotenv import load_dotenv, find_dotenv

class Config:
    load_dotenv(find_dotenv())
    
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PROPAGATE_EXCEPTIONS = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = [
        "access",
        "refresh",
    ]
    JWT_ACCESS_TOKEN_EXPIRES = 1800

    SWAGGER = {"openapi": "3.0.0"}

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URI")
    


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
    