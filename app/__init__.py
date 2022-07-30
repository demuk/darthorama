from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_ckeditor import CKEditor
from flask_mail import Message, Mail

app = Flask(__name__)
app.config.from_object(Config)
ckeditor = CKEditor(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
moment = Moment(app)
login.login_view = 'login'
mail = Mail(app)


from app import routes, models
