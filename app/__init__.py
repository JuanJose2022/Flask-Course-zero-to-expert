from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
def create_app():
    app = Flask(__name__) #Refering the flask server to this archive
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    return app