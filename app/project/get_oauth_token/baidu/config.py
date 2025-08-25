from tk_base_utils import load_toml
from pathlib import Path


class BaiduConfigManager:
    def __init__(self, config_path: str|Path = "config.toml"):
        if isinstance(config_path, str):
            config_path = Path(config_path)
        self._config = load_toml(config_path)

    @property
    def access_token_url(self):
        return self._config['oauth']['baidu'].get('access_token_url')

    @property
    def max_retry(self):
        return self._config.get("retry",{}).get('max_retry', 3)
    
    @property
    def retry_delay(self):
        return self._config.get("retry",{}).get('retry_delay', 60)
    
    def mapping_name_id(self,item:str|int):
        return self._config['oauth']['baidu']['name_id_map'].get(str(item))
    
_baidu_config_manager = None
# 单例模式
def get_baidu_config(config_path: str|Path = "config.toml") -> BaiduConfigManager:
    global _baidu_config_manager
    if _baidu_config_manager is None:
        _baidu_config_manager = BaiduConfigManager(config_path)
    return _baidu_config_manager

# 延迟加载
class BaiduConfigProxy:
    def __getattr__(self, name: str):
        return getattr(get_baidu_config(), name)
    

baidu_config:BaiduConfigManager = BaiduConfigProxy()
