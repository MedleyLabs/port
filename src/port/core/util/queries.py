from ..port.core.models import Plugin


def get_active_plugins():
    """ Returns all active plugins """
    return Plugin.query.filter(Plugin.is_active).all()
