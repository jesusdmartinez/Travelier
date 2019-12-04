from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .config import DevelopmentConfig
db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=False)
login = LoginManager(app)

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config['SECRET_KEY'] = 'you-will-never-guess'
    app.config.from_object(DevelopmentConfig)
    login = LoginManager(app)
    db.init_app(app)


    with app.app_context():

        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        return app

