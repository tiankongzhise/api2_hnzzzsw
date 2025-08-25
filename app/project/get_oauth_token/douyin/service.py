from .core import douyin_oauth
from .database import update_douyin_oauth_credentials
from .logger import logger,logger_wrapper
from .models import DouyinCallbackParams
from fastapi import APIRouter,Request

douyin_oauth_router = APIRouter()

@douyin_oauth_router.api_route("/douyin", methods=["GET", "POST"])
async def get_douyin_oauth_token(request: Request):
    logger.info_service('get_douyin_oauth_token is runing!')
    params = DouyinCallbackParams(**dict(request.query_params))
    logger.info_service(f'params:{params}')
    oauth_result = douyin_oauth(params)
    if oauth_result.status == 'success':
        db_operation_result = update_douyin_oauth_credentials(oauth_result.data)
    logger.info_service(f'抖音授权认证数据库插入结果为:{db_operation_result}')
    return oauth_result

