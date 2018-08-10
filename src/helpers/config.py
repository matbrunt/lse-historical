import os
import yaml
from configparser import ConfigParser

from helpers import utils


def read_config():
    config = yaml.load(open(utils.get_project_path('config.yaml')))
    
    # Override config setting with environment variable, if it exists
    env_config = os.getenv('DEBUG', None)
    if env_config is not None:
        config['debug'] = env_config.lower() == 'true'

    return config


def read_credentials(section=None):
    credentials = ConfigParser(interpolation=None)
    credentials.read(utils.get_project_path('credentials.txt'))

    if section is None:
        return credentials
    return credentials[section]
