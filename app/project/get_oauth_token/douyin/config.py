from tk_base_utils import load_toml,find_file
from pathlib import Path




class DouyinConfigManager:
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



_douyin_config_manager = None
# 单例模式
def get_douyin_config(config_path: str|Path = "config.toml") -> DouyinConfigManager:
    global _douyin_config_manager
    if _douyin_config_manager is None:
        _douyin_config_manager = DouyinConfigManager(config_path)
    return _douyin_config_manager
