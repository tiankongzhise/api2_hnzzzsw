from pydantic import BaseModel, ConfigDict


def to_camel_case(snake_str: str) -> str:
    """将下划线命名转换为驼峰命名"""
    components = snake_str.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


class BaiduOauthParams(BaseModel):
    app_id: str
    auth_code: str
    user_id: str
    state: str
    timestamp: str
    signature: str
    
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel_case
    )
class BaiduAccessTokenParams(BaseModel):
    appId: str
    authCode: str
    secretKey: str
    grantType: str = "auth_code"
    userId: str

class BaiduAccessToken(BaseModel):
    access_token:str
    refresh_token:str
    open_id:str
    expires_time:str
    refresh_expires_time:str
    user_id:int
    
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel_case
    )
    
class TransformAuthCodeResponse(BaseModel):
    status:str
    message:str
    data:BaiduAccessToken|None
