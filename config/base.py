import os

class BaseConfig(object):
    WEB_CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']

    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )

    # configure celery to work with redis
    CELERY_RESULT_BACKEND = 'redis://{0}:{1}'.format(
        os.environ['REDIS_PORT_6379_TCP_ADDR'],
        os.environ['REDIS_PORT_6379_TCP_PORT']
    )
    CELERY_BROKER_URL = CELERY_RESULT_BACKEND

    # for Flask-Webhooks extension
    GITHUB_WEBHOOKS_KEY = os.environ['GITHUB_SECRET']
    VALIDATE_IP = False
    VALIDATE_SIGNATURE = True