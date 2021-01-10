from decouple import config

DEBUG = config('DEBUG',default=True, cast=bool)
TESTING = config('TESTING',default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='__my_strong_secret_key__')
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI', default='postgres://postgres:postgres@postgres:5432/test')
SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)