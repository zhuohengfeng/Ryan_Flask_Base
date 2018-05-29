

import os, sys
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
sys.path.append(os.path.join(ABSPATH, 'restful'))


from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app.admin import admin
#from flask_mail import Mail
import config

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(admin)

# Restful api
api = Api(app)

# Load extensions
db = SQLAlchemy()
db.init_app(app)

bootstrap = Bootstrap(app)

# mail = Mail()
# mail.init_app(app)

from . import views
print(sys.path)
from restful.ap import *





