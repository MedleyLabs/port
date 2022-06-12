from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """ Home page """
    return render_template('layout.html')
