import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_DIR_PATH = BASE_PATH + os.sep + "OutPut"

LOGFILE_DIR_PATH = OUTPUT_DIR_PATH + os.sep + "log_file"

LOG_FILE_PATH = LOGFILE_DIR_PATH + os.sep + "log.log"

SCREENSHOT_DIR_PATH = OUTPUT_DIR_PATH + os.sep + "screenshot"

LOCATOR_DIR_PATH = BASE_PATH + os.sep + "PageLocator"

CONFIG_DIR_PATH = BASE_PATH + os.sep + "Config"
CONFIG_FILE_PATH = CONFIG_DIR_PATH + os.sep + "config.conf"
YAML_FILE_PATH = CONFIG_DIR_PATH + os.sep + "yaml.yaml"


print(SCREENSHOT_DIR_PATH)