from tk_base_utils import load_toml,find_file
from pathlib import Path
from dotenv import load_dotenv



class DouyinConfigManager:
    _instance = None
    
    def __new__(cls, config_path: str|Path = "config.toml"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, config_path: str|Path = "config.toml"):
        self.env_path = find_file('.env')
        if isinstance(config_path, str):
            config_path = find_file(config_path)
        if not config_path.exists():
            raise FileNotFoundError(f"config file not found: {config_path}")
        if not self.env_path.exists():
            raise FileNotFoundError(f"env file not found: {self.env_path}")
        self.config_path = config_path
        self._config = load_toml(self.config_path)
        load_dotenv(self.env_path)
    @property
    def http_config(self):
        return self._config.get("http_config",{})
    
    @property
    def access_token_query_url(self):
        return self._config['oauth']['douyin']['access_token_query_url']
    
    def mapping_name_id(self,item):
        return self._config['oauth']['baidu']['name_id_map'].get(str(item))
    
    
    def reload_config(self,config_path: str|Path|None = "config.toml"):
        from .logger import get_douyin_logger
        logger = get_douyin_logger()
        logger.info_config(f"reload config file: {self.config_path}")
        try:
            if config_path is None:
                self._config = load_toml(self.config_path)
                logger.info_config('douyin认证功能设置重载成功')
                return True
            if isinstance(config_path, str):
                config_path = find_file(config_path)
            if not config_path.exists():
                logger.error(f"reload douyin config error!config file not found: {config_path}")
                return False
            self.config_path = config_path
            self._config = load_toml(self.config_path)
            logger.info_config(f"抖音认证重载配置文件成功: {self.config_path}")
            return True
        except Exception as e:
            logger.error(f"抖音认证重载配置文件失败: {config_path},错误信息:{e}")
            return False


# 单例模式
def get_douyin_config(config_path: str|Path = "config.toml") -> DouyinConfigManager:
    return DouyinConfigManager(config_path)

def reload_douyin_config():
    get_douyin_config().reload_config()
