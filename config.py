import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'darthorama.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kjfdkjfkdjfkdjfkdkdklfjlksjdfkldjfkldf'
    CKEDITOR_PKG_TYPE = 'full-all'
    MAIL_SERVER: 'smtp.office365.com'
    MAIL_PORT: 465
    MAIL_USE_TLS: True
    MAIL_USE_SSL: False
    MAIL_USERNAME: "kiptoodennismutai@outlook.com"
    MAIL_PASSWORD: "kiptoodennis123" 