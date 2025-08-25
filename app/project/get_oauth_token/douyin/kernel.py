from tk_base_utils.tk_http import ClientConfig,HttpClient
from .config import get_douyin_config
from .models import DouyinOauth2AccessTokenParams
from .logger import logger_wrapper

class DouyinHttpClient(object):
    def __init__(self):
        self._douyin_config = get_douyin_config()
        self._http_client = HttpClient(self._load_http_config())
    
    def _load_http_config(self,headers:dict|None=None,user_agent:str|None=None):
        """加载HTTP配置"""
        http_config = self._douyin_config.http_config
        http_config['headers'] ={ "Content-Type": "application/json"} if headers is None else headers
        http_config['user_agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0' if user_agent is None else user_agent
        return ClientConfig(**http_config)
    
    @logger_wrapper(level="INFO_KERNEL")
    def oauth2_access_token(self,params:DouyinOauth2AccessTokenParams):
        url = self._douyin_config.access_token_query_url
        resp = self._http_client.post(url,json = params.model_dump())
        resp.raise_for_status()
        return resp.json()
