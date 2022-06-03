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

        # Built-in routes (import here to avoid circular dependencies)
        from port.core.routes import category
        from port.core.routes import errorhandlers
        from port.core.routes import main
        from port.core.routes import plugin
        from port.core.routes import userauth

        # Built-in blueprints
        app.register_blueprint(category)
        app.register_blueprint(errorhandlers)
        app.register_blueprint(main)
        app.register_blueprint(plugin)
        app.register_blueprint(userauth)

        from port.carbon_offset.routes import carbon_offset
        plugin_blueprints = [carbon_offset]

        for blueprint in plugin_blueprints:
            app.register_blueprint(blueprint)

    return app
