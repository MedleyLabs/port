from flask import Blueprint, render_template

from ..port.core.models import Category


category = Blueprint('category', __name__)


@category.route('/category/<int:category_id>/')
def plugins_by_category(category_id):
    """Returns plugins, category for a specific category"""
    filtered_categories = Category.query.filter_by(id=category_id)
    category = filtered_categories[0]
    return render_template('main.html', title=category.name,
                           categories=filtered_categories,
                           plugins=category.plugins)
