from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app.admin import admin
#from flask_mail import Mail
import config

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(admin)

# Load extensions
db = SQLAlchemy()
db.init_app(app)

bootstrap = Bootstrap(app)

# mail = Mail()
# mail.init_app(app)

from . import views



