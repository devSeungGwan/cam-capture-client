import logging
import logging.config
from fvcore.common.config import CfgNode as CN

from cam_capture_client.common import read_json

class Logger:
    def __init__(self, cfg: CN):
        __logger_conf = read_json(cfg.LOGGER.CONF_PATH)
        logging.config.dictConfig(__logger_conf)

        self.__logger = logging.getLogger(cfg.LOGGER.NAME)
    
    def info(self, msg: str):
        self.__logger.info(msg)
        
    def debug(self, msg: str):
        self.__logger.debug(msg)
        
    def warning(self, msg: str):
        self.__logger.warning(msg)
    
    def error(self, msg: str):
        self.__logger.error(msg)
    
    def critical(self, msg: str):
        self.__logger.critical(msg)
