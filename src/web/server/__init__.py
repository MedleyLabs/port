import config  # noqa:E401
from faker import Faker
from flask import Flask
from flask_login import LoginManager
from flask import request, render_template
import os

app = Flask(__name__)

# Environment Configuration
app.config.from_object('config.settings.' + os.environ['ENV'])

# User Session Management
login_manager = LoginManager(app)

# Database
from .models import db, user, category, item, plant, shortcut, ma, substances
db.create_all()
db.session.commit()

# Seed Users and Categories in Database
# if app.config['TESTING'] is True:
#     fake = Faker()
#
#     for _ in range(5):
#         user.User.seed(fake)
#
#     for _ in range(70):
#         category.Category.seed(fake)


# server.routes
from server.routes.electrodermal import electrodermal
from server.routes.userauth import userauth
from server.routes.category import category
from server.routes.item import item
from server.routes.main import main
from server.routes.plant import plant
from server.routes.shortcut import shortcut
from server.routes.substances import substances
from server.routes.errorhandlers import errorhandlers

# register_blueprint
app.register_blueprint(electrodermal)
app.register_blueprint(userauth)
app.register_blueprint(category)
app.register_blueprint(item)
app.register_blueprint(main)
app.register_blueprint(plant)
app.register_blueprint(shortcut)
app.register_blueprint(substances)
app.register_blueprint(errorhandlers)

if __name__ == '__main__':
    app.run()
