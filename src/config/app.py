import os

class Environment():
    """
    Configure your envorimment for developer
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = '__my_strong_secret_key__'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@postgres:5432/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False