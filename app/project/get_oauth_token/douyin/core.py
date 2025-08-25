from .logger import logger,logger_wrapper
from .kernel import DouyinHttpClient
from .models import DouyinCallbackParams,DouyinAuthResponse,DouyinOauthCredentials,DouyinOauth2AccessTokenParams
from .config import get_douyin_config

import os
from datetime import datetime, timedelta

@logger_wrapper(level="INFO_UTILS")
def _calculate_expires_time(time_delta: int) -> str:
    return (datetime.now() + timedelta(seconds=time_delta)).strftime('%Y-%m-%d %H:%M:%S')

@logger_wrapper(level="INFO_CORE")
def _Response2DTO(responese:dict) -> DouyinAuthResponse:
    if responese['code'] != '0':
        return DouyinAuthResponse(
            status='error',
            msg=responese['msg'],
        )
    douying_config = get_douyin_config()
    advertiser_ids = responese['data']['advertiser_ids']
    control_name = ''
    control_id = ''
    for id in advertiser_ids:
        if douying_config.mapping_name_id(str(id)) is None:
            continue
        control_name = douying_config.mapping_name_id(str(id))
        control_id = str(id)
        break
    if control_name == '':
        return DouyinAuthResponse(
            status='error',
            msg=f'未找到抖音巨量超级管理员,请检查配置文件,返回的advertiser_ids:{advertiser_ids}'
        )
    return DouyinAuthResponse(
        status='success',
        msg='success',
        data=DouyinOauthCredentials(
            access_token=responese['data']['access_token'],
            expires_time=_calculate_expires_time(responese['data']['expires_in']),
            refresh_token=responese['data']['refresh_token'],
            refresh_expires_time=_calculate_expires_time(responese['data']['refresh_token_expires_in']),
            controler_id=control_id,
            controler_name=control_name,
        )
    )
    

    
@logger_wrapper(level="INFO_CORE")
def douyin_oauth(callback_params:DouyinCallbackParams):
    http_client = DouyinHttpClient()
    params = DouyinOauth2AccessTokenParams(
        app_id=callback_params.app_id,
        auth_code=callback_params.auth_code,
        secret=os.getenv("DOUYIN_APP_SECRET_KEY"),
    )
    resp = http_client.oauth2_access_token(params)
    return _Response2DTO(resp)
