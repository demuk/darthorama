import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'darthorama.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kjfdkjfkdjfkdjfkdkdklfjlksjdfkldjfkldf'
    CKEDITOR_PKG_TYPE = 'full-all'

