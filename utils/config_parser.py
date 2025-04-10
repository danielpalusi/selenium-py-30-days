import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
    # "with" statement is used to wrap the execution of a block with methods defined by a context manager

config = load_config()