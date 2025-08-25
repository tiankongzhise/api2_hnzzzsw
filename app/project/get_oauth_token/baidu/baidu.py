
import os
import httpx
import asyncio
from fastapi import Request,APIRouter
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from tk_base_utils import load_toml,get_target_file_path
from sqlalchemy import select
from tk_db_utils import get_db_client
from tk_db_utils import DbOrmBaseMixedIn

from ....log import create_logger
from .models import BaiduOauthParams,TransformAuthCodeResponse,BaiduAccessToken,BaiduAccessTokenParams
from .schemas import OauthCredentialsTable
from .config import get_baidu_config


load_dotenv()

logger = create_logger(__file__)

baidu_oauth_router = APIRouter()

baidu_config = get_baidu_config('config.toml')

async def _transform_auth_code_to_access_token(secret_key:str,params:BaiduOauthParams) -> TransformAuthCodeResponse:
    logger.info(f'_transform_auth_code_to_access_token is running')
    try:
        access_token_params = BaiduAccessTokenParams(
            appId=params.app_id,
            authCode=params.auth_code,
            secretKey=secret_key,
            userId=params.user_id,
        )
    except Exception as e:
        logger.error(f"_transform_auth_code_to_access_token  BaiduAccessTokenParams error,BaiduOauthParams:{params}")
        return TransformAuthCodeResponse(
            status="params trans error",
            message="将auth_code转换为access_token失败,BaiduOauthParams转换为BaiduAccessTokenParams失败",
            data=None
        )
    
    
    api_url = baidu_config.access_token_url
    if not api_url:
        logger.error(f"_transform_auth_code_to_access_token  api_url is None")
        return TransformAuthCodeResponse(
            status="api url is None",
            message="将auth_code转换为access_token失败,api_url is None",
            data=None
        )
    

    async with httpx.AsyncClient() as client:
        url = f"{api_url}"
        headers = {
            "Content-Type": "application/json;charset:utf-8;",
        }

        logger.info(f"api request to {url}")

        try:
            response = await client.request(
                method="post",
                url=url,
                headers=headers,
                json=access_token_params.model_dump(),
                timeout=30.0,
            )

            logger.info(f"Received response with status code {response.status_code}")
            
            if response.status_code != 200:
                logger.info("进入状态码错误处理分支")
                try:
                    error_json = response.json()
                except Exception:
                    error_json = "Invalid JSON response"
                if isinstance(error_json,str):
                    logger.info(f"将auth_code转换为access_token失败,query error,response_text:{response.text}")
                else:
                    logger.info(f"将auth_code转换为access_token失败,query error,response_json:{error_json}")

                return TransformAuthCodeResponse(
                    status="query error",
                    message=f"将auth_code转换为access_token失败,status_code:{response.status_code},response:{error_json},response_text:{response.text}",
                    data=None
                )
            
            logger.info("状态码为200，开始解析响应数据")
            response_json = response.json()
            # 安全检查响应格式
            if 'code' not in response_json:
                return TransformAuthCodeResponse(
                    status="query error",
                    message=f"将auth_code转换为access_token失败,响应格式错误：缺少code字段,response:{response_json}",
                    data=None
                )
            if response_json['code'] != 0:
                error_message = response_json.get('message', '未知错误')
                return TransformAuthCodeResponse(
                    status="query error",
                    message=f"将auth_code转换为access_token失败,query fail,faile reason:{error_message}",
                    data=None
                )
            
            # 检查成功响应的data字段
            if 'data' not in response_json:
                return TransformAuthCodeResponse(
                    status="query error",
                    message=f"将auth_code转换为access_token失败,响应格式错误：缺少data字段,response:{response_json}",
                    data=None
                )
            
            try:
                response_data = BaiduAccessToken(**response_json['data'])
            except Exception as e:
                return TransformAuthCodeResponse(
                    status="query error",
                    message=f"将auth_code转换为access_token失败,数据格式错误：{e},response_data:{response_json['data']}",
                    data=None
                )
            
            return TransformAuthCodeResponse(
                status="success",
                message="将auth_code转换为access_token成功",
                data=response_data
            )
        except httpx.RequestError as e:
            logger.error(f"Request to {url} failed: {e}")
            return TransformAuthCodeResponse(
                status="request error",
                message=f"将auth_code转换为access_token失败,httpx.RequestError,异常信息:{e}",
                data=None
            )
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return TransformAuthCodeResponse(
                status="unexpected error",
                message=f"将auth_code转换为access_token失败,Exception,异常信息:{e}",
                data=None
            )
        



async def transform_auth_code_to_access_token(params:BaiduOauthParams):
    """
    将baidu临时授权码转化为access_token
    :param 
        params:
        BaiduOauthParams(
            app_id: str
            auth_code: str
            user_id: str
            state: str
            timestamp: str
            signature: str
            )
    :return:
        TransformAuthCodeResponse(
            status:str
            message:str
            data:BaiduAccessToken
        )
    """
    logger.info('transform_auth_code_to_access_token is runing!')
    secret_key = os.getenv('BAIDU_APP_SECRET_KEY')
    if not secret_key:
        logger.error(f"transform_auth_code_to_access_token  secret_key is None")
        return TransformAuthCodeResponse(
            status="error",
            message="将auth_code转换为access_token失败,secret_key is None",
            data=None
        )
    retry_count = 0
    max_retry = baidu_config.max_retry
    retry_delay = baidu_config.retry_delay
    
    while retry_count<max_retry:
        response = await _transform_auth_code_to_access_token(secret_key,params)
        if response.status == "request error":
            retry_count += 1
            logger.warning(f"transform_auth_code_to_access_token  request error:{response.message}, retry_count:{retry_count}")
            await asyncio.sleep(retry_delay)
            continue
        else:
            return response
    
    logger.error(f"transform_auth_code_to_access_token  request error after {max_retry} retries, last error message: {response.message}")
    return response
    

@baidu_oauth_router.api_route("/baidu", methods=["GET", "POST"])
async def get_baidu_oauth_token(request: Request):
    logger.info('get_baidu_oauth_token is runing!')
    params = BaiduOauthParams(**dict(request.query_params))
    logger.info(f'params:{params}')
    response = await transform_auth_code_to_access_token(params)
    logger.info(f'response:{response}')
    db_operation_result = 'init'
    if response.status == "success":
        try:
            env_path = get_target_file_path('.env')
            db_config_path = get_target_file_path('config.toml')
            logger.info(f'env_path:{env_path}')
            logger.info(f"db_config_path:{db_config_path}")
            db_client = get_db_client(env_file_path=env_path,db_config_path=db_config_path,database=DbOrmBaseMixedIn)
            
            logger.info("数据库初始化成功!")
            controler_id = str(response.data.user_id)
            controler_name = baidu_config.mapping_name_id(controler_id)
            logger.info("开始尝试获取session!")
            with db_client.session_scope as session:
                logger.debug('session is in!')
                stmt = select(OauthCredentialsTable).where(OauthCredentialsTable.controler_id == controler_id)
                result = session.execute(stmt)
                if result.first():
                    logger.info(f"get_baidu_oauth_token  controler_id:{controler_id} already exist")
                    item = session.scalars(stmt).one()
                    item.oauth_credentials = response.data.model_dump()
                    db_operation_result = 'update'
                    logger.info(f"controler_id:{controler_id},controler_name:{controler_name} is update")
                else:                
                    oauth_credentials = OauthCredentialsTable(
                        controler_id=controler_id,
                        controler_name=controler_name,
                        channel="baidu",
                        oauth_credentials=response.data.model_dump(),
                    )
                    session.add(oauth_credentials)
                    db_operation_result = 'insert'
                    logger.info(f"controler_id:{controler_id},controler_name:{controler_name} is update")
        except Exception as e:
            logger.error(f"get_baidu_oauth_token add database error,{e}")
            db_operation_result = 'fail'
    result = response.model_dump()
    result['db_operation_result'] = db_operation_result
    logger.info(f'result is {result}')
    return JSONResponse(content=result)



