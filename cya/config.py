import os

SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
#DEBUG = os.environ.get('DEBUG')
#ENV = os.environ.get('ENV')
