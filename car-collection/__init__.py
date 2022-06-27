from flask import Flask
from .main_site.routes import main
from .auth.routes import auth
from config import Config


app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(auth)
app.config.from_object(Config)