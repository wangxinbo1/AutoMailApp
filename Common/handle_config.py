from configparser import ConfigParser
from Common.dir_path import CONFIG_FILE_PATH
class HandleConfig():
    def __init__(self, config_name):
        self.config_name = config_name
        self.do_config = ConfigParser()
        self.do_config.read(self.config_name, encoding="utf-8")

    def get_value(self, section, option):
        return self.do_config.get(section, option)


do_config = HandleConfig(CONFIG_FILE_PATH)

