from tk_base_utils.tk_logger import set_logger_config_path, get_logger,create_logger_wrapper,reload_logger
from tk_base_utils.tk_logger.logger import EnhancedLogger
from .config import get_douyin_config



set_logger_config_path(get_douyin_config().config_path)
logger: EnhancedLogger = get_logger(mode="multi",instance_name="douyin_oauth")
logger_wrapper = create_logger_wrapper(logger)

def get_douyin_logger() -> EnhancedLogger:
    return logger

def reload_douyin_logger():
    reload_logger(instance_name="douyin_oauth")
