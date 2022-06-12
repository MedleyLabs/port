from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from port.system.files import import_plugins

login_manager = LoginManager()
db = SQLAlchemy()
ma = Marshmallow()


# Command-line options: port
#
#   port install ...       Installs a plugin (alias port pip install ... to port/plugins + restart Flask via blue/green deployment
#


def initialize_app():
    """ Initializes the Flask app """

    app = Flask(__name__)

    app.config.from_object('config.settings.Development')  # TODO

    login_manager.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        # Routes must be imported here to avoid circular dependencies
        from port.routes import (
            category,
            errorhandlers,
            main,
            plugin,
            auth
        )

        app.register_blueprint(category)
        app.register_blueprint(errorhandlers)
        app.register_blueprint(main)
        app.register_blueprint(plugin)
        app.register_blueprint(auth)

        # import_plugins()
        # register_blueprints()

        # plugin_blueprints = find_plugin_blueprints()
        #
        # for blueprint in plugin_blueprints:
        #     app.register_blueprint(blueprint)

        from port.models import User
        user = User(
            username='curioushuman',
            first_name='Eric',
            middle_name='Davis',
            last_name='Yates'
        )
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

    return app
