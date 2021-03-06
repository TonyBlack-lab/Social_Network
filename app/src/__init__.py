from app import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, template_folder="../templates")

app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.src import entity, form, controller
