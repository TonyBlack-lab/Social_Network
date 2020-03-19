from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask (__name__) # Переменная __name__, переданная в класс Flask,
                       # как отправнуя точку, когда ему необходимо загрузить связанные ресурсы, такие как файлы шаблонов
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)
migrate = Migrate(app, db) # migrate представляет механизм миграции; объект db, который представляет базу данных

from app import routes, models # модуль models определит структуру базы данных

