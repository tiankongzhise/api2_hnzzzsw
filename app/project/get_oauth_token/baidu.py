
from ...log import create_logger
from .router import oauth_router

logger = create_logger(__file__)

@oauth_router.get("/baidu")
async def get_baidu_oauth_token():
    return {'status':'success','data':'模拟百度oauth token处理成功'}



