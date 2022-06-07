import glob
import importlib
import os
import pkgutil

import port.plugins


def iter_namespace(pkg):
    """ """
    return pkgutil.iter_modules(pkg.__path__, pkg.__name__ + '.')


def import_plugins():
    """"""
    for _, name, _ in iter_namespace(port.plugins):
        importlib.import_module(name)


def register_blueprints():
    """ """




def find_plugins():
    """ Finds all Python packages inside the port.plugins directory """
    return [os.path.join(importer.path, name) for importer, name, ispkg in pkgutil.iter_modules(plugins.__path__) if ispkg]


def find_plugin_modules(plugin_path):
    return glob.glob(os.path.join(plugin_path, "**/*.py"), recursive=True)


def find_plugin_functions(plugin_path):
    return


def find_plugin_blueprints():
    """ Discovers all the blueprints defined in plugins """

    plugins = find_plugins()

    for plugin in plugins:

        print('PLUGIN', plugin)

        modules = find_plugin_modules(plugin)

        for module in modules:
            print(module, dir(port.plugins.carbon_offset.routes))


def register_plugin_routes():
    """ Finds all functions decorated by the plugin_route decorator """

    # plugin_paths = find_plugins()
    #
    # for plugin_path in plugin_paths:
    #
    #     print('\nPlugin:', plugin_path, '\n')
    #
    #     module_paths = find_plugin_packages(plugin_path)
    #
    #     for package_path in package_paths:
    #         print('\tPackage:', package_path)
    #
    #         module_paths = find_plugin_modules(package_path)
    #
    #         for module_path in module_paths:
    #             print('\t\tModule: ', module_path)
    #
    #     print('\n')
