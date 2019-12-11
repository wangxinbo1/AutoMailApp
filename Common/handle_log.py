import logging
from Common.handle_config import do_config
import os
from Common.dir_path import LOGFILE_DIR_PATH

class HandleLog():
    def __init__(self):
        self.logger = logging.getLogger(do_config.get_value("Log", "log_collector_name"))
        self.logger.setLevel(do_config.get_value("Log", "log_collector_level"))
        # 定义日志输出渠道
        console = logging.StreamHandler()

        file = logging.FileHandler(os.path.join(LOGFILE_DIR_PATH, do_config.get_value("Log", "log_file_name")), encoding="utf8")
        #定义日志输出渠道等级
        console.setLevel(do_config.get_value("Log", "log_console_level"))
        file.setLevel(do_config.get_value("Log", "log_file_level"))
        # 定义日志的输出格式
        simple_format = logging.Formatter(do_config.get_value("Log", "log_simple_format"))
        complex_format = logging.Formatter(do_config.get_value("Log", "log_complex_format"))
        #对接日志渠道和格式
        console.setFormatter(simple_format)
        file.setFormatter(complex_format)

        #对接日志渠道和日志收集器
        self.logger.addHandler(console)
        self.logger.addHandler(file)

    def get_logger(self):
        return self.logger

logger = HandleLog().get_logger()