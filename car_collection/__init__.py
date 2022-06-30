from flask import Flask
from .main_site.routes import main
from .auth.routes import auth
from .api.routes import api
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db as root_db
from .models import login_manager, ma

from flask_marshmallow import Marshmallow

from flask_cors import CORS

from car_collection.helpers import JSONEncoder

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(api)
app.register_blueprint(auth)
app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app, root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)