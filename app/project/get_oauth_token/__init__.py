from .router import oauth_router
from . import baidu  # 导入 baidu 模块以注册路由

__all__ = [
    "oauth_router"
]
