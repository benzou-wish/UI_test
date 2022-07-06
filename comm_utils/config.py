import os
from configparser import ConfigParser


class ConfigReader:
    def __init__(self, env):
        self.cf = ConfigParser()
        self.env = env.upper()
        self.cf.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/env.conf'))

    @property
    def config(self):
        return dict(self.cf.items(self.env))

    @property
    def base_url(self):
        return self.config['base_url']


if __name__ == "__main__":
    c = ConfigReader('QA')
    print(c.config)

