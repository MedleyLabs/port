from flask import (
    abort,
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for
)
from flask_login import current_user, login_required
from sqlalchemy import func

from port import db
from port.core.models import Plugin
# from port.forms.plugin import PluginForm

plugin = Blueprint('plugin', __name__)


@plugin.route("/plugin/create", methods=['GET', 'POST'])
@login_required
def create_plugin():
    """CREATE Plugin"""
    form = PluginForm()
    if form.validate_on_submit():
        new_plugin = Plugin(name=form.name.data,
                            description=form.description.data,
                            category=form.category.data,
                            user=current_user)
        db.session.add(new_plugin)
        db.session.commit()
        flash('Your job listing has been successfully created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('plugin.html', form=form)


@plugin.route("/plugin/<int:plugin_id>/update", methods=['GET', 'POST'])
@login_required
def update_plugin(plugin_id):
    """
    UPDATE Plugin
    :param plugin_id: plugin_id (int) for Plugin
    """
    plugin = Plugin.query.get_or_404(plugin_id)
    if plugin.user != current_user:
        abort(403)
    form = PluginForm()
    if form.validate_on_submit():
        plugin.name = form.name.data
        plugin.description = form.description.data
        plugin.category = form.category.data
        plugin.time_updated = func.now()
        db.session.commit()
        flash('Your job listing has been successfully updated!', 'success')
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.name.data = plugin.name
        form.description.data = plugin.description
        form.category.data = plugin.category
    return render_template('plugin.html', form=form)


@plugin.route("/plugin/<int:plugin_id>/delete", methods=['POST'])
@login_required
def delete_plugin(plugin_id):
    """
    DELETE Plugin
    :param plugin_id: plugin_id (int) for Plugin
    """
    plugin = Plugin.query.get_or_404(plugin_id)
    if plugin.user != current_user:
        abort(403)
    db.session.delete(plugin)
    db.session.commit()
    flash('Your job listing has been successfully deleted!', 'success')
    return redirect(url_for('main.index'))
