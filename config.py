import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'db.sqlite3')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
    #    or 'sqlite:///' + str(BASE_DIR / 'data' / 'db.sqlite3')
    # if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-never-know'
