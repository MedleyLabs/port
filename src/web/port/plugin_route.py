import __main__
import os

from flask import Blueprint


def plugin_route(rule, **options):

    print('RULE', rule)

    def decorator(func):
        """
        This decorator

        """

        print('FUNC', func)

        from port.app import app

        module_name = func.__module__

        if module_name == '__main__':
            module_name = __main__.__file__

        blueprint_name = module_name.split('.')[-2]

        print('Inside')
        print('module_name', module_name)
        print('blueprint_name', blueprint_name)

        blueprint_registered = blueprint_name in app.blueprints.keys()
        blueprint = Blueprint(blueprint_name, module_name)

        print(app.blueprints.keys())

        blueprint.route(rule)(func)

        if not blueprint_registered:
            print('Registering blueprint...')
            app.register_blueprint(blueprint)

        print(blueprint.deferred_functions)

        # def inner(*args, **kwargs):
        #     return func(*args, **kwargs)
        # return inner
    return decorator

