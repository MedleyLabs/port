import sys

from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


sys.path.insert(0, '/home/eric/port/src/port')  # TODO REMOVE

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

        # Built-in routes (import here to avoid circular dependencies)
        from port.core.routes import category
        from port.core.routes import errorhandlers
        from port.core.routes import main
        from port.core.routes import plugin
        from port.core.routes import userauth

        # Import routes here
        from port.plugins.carbon_offset.routes import carbon_offset

        # Built-in blueprints
        app.register_blueprint(category)
        app.register_blueprint(errorhandlers)
        app.register_blueprint(main)
        app.register_blueprint(plugin)
        app.register_blueprint(userauth)

        # Register blueprints here
        app.register_blueprint(carbon_offset)

    return app
