import os
import yaml

current_directory = os.path.dirname(__file__)
config_path = os.path.join(current_directory, 'config.yml')

with open(config_path, 'r') as f:
    config = yaml.safe_load(f)
