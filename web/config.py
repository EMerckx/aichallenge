import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = False
SECRET_KEY = 'badass'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
