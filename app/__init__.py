from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from app.auth import auth
def create_app():
    app = Flask(__name__) #Refering the flask server to this archive
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    return app