from .router import oauth_router
from .baidu import baidu_oauth_router  
from .douyin import douyin_oauth_router

oauth_router.include_router(baidu_oauth_router)
oauth_router.include_router(douyin_oauth_router)

__all__ = [
    "oauth_router"
]
