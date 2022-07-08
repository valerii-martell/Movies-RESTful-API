import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")

class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'db.sqlite3')

    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{url}/{db}'.\
        format(user='postgres',pw='passwd',url='localhost',db='movies_api_db')

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
    #    or 'sqlite:///' + str(BASE_DIR / 'data' / 'db.sqlite3')
    # if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-never-know'
