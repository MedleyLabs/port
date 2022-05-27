from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """ Home page """
    return 'Hello port!'
