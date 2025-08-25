from tk_base_utils.tk_logger import set_logger_config_path, get_logger,logger_wrapper_multi
from tk_db_utils.logger import logger_wrapper

from .config import get_douyin_config


set_logger_config_path(get_douyin_config().config_path)
logger = get_logger(mode="multi",name="douyin_oauth")
logger_wrapper = logger_wrapper_multi(logger)
