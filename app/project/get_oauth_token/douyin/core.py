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
    # 检查响应是否包含错误信息
    if 'message' in responese and responese['message'] == 'error':
        # 处理错误响应格式: {'data': {'error_code': 4, 'description': '参数错误'}, 'message': 'error'}
        error_msg = responese.get('data', {}).get('description', '未知错误')
        return DouyinAuthResponse(
            status='error',
            message=error_msg,
        )
    # 检查旧格式的错误响应
    if 'code' in responese and responese['code'] != '0':
        return DouyinAuthResponse(
            status='error',
            message=responese.get('msg', '未知错误'),
        )
    # 检查成功响应格式
    if 'data' not in responese:
        return DouyinAuthResponse(
            status='error',
            message='响应格式错误：缺少data字段',
        )
    
    data = responese['data']
    required_fields = ['advertiser_ids', 'access_token', 'expires_in', 'refresh_token', 'refresh_token_expires_in']
    for field in required_fields:
        if field not in data:
            return DouyinAuthResponse(
                status='error',
                message=f'响应格式错误：缺少{field}字段',
            )
    
    douying_config = get_douyin_config()
    advertiser_ids = data['advertiser_ids']
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
            message=f'未找到抖音巨量超级管理员,请检查配置文件,返回的advertiser_ids:{advertiser_ids}'
        )
    return DouyinAuthResponse(
        status='success',
        message='success',
        data=DouyinOauthCredentials(
            access_token=data['access_token'],
            expires_time=_calculate_expires_time(data['expires_in']),
            refresh_token=data['refresh_token'],
            refresh_expires_time=_calculate_expires_time(data['refresh_token_expires_in']),
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
