import os
import sys

from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()
ma = Marshmallow()


def initialize_app():
    """ Initializes the Flask app """

    app = Flask(__name__)

    app.config.from_object('config.settings.Development')  # TODO

    login_manager.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        # Built-in routes
        from .routes.category import category
        from .routes.errorhandlers import errorhandlers
        from .routes.main import main
        from .routes.plugin import plugin
        from .routes.userauth import userauth

        # Import routes here

        # Built-in blueprints
        app.register_blueprint(category)
        app.register_blueprint(errorhandlers)
        app.register_blueprint(main)
        app.register_blueprint(plugin)
        app.register_blueprint(userauth)

        # Register blueprints here

    return app


if __name__ == '__main__':
    app.run()
