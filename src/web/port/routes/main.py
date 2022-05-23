from flask import Blueprint, render_template, jsonify
from flask_login import current_user

from port.models.category import Category, CategorySchema
from port.models.plugin import Plugin


main = Blueprint('main', __name__)


@main.route('/')
def index():
    """ Home page """
    return 'Hello port!'
