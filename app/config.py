import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLE = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get ('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
                                           # SQLAlchemy принимает местоположение базы данных приложения
    SQLALCHEMY_TRACK_MODIFICATIONS = False     # в значение False, чтобы отключить функцию Flask-SQLAlchemy, она сигнализирует
                                           # каждый раз, когда в базе данных должно быть внесено изменение

