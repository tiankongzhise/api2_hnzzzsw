from pydantic import BaseModel,field_validator
from datetime import datetime


class DouyinCallbackParams(BaseModel):
    app_id: int
    auth_code: str
    uid: str

class DouyinOauth2AccessTokenParams(BaseModel):
    app_id: int
    auth_code: str
    secret: str

class DouyinOauthCredentials(BaseModel):
    access_token: str
    expires_time: str
    refresh_token: str
    refresh_expires_time: str
    controler_id: str
    controler_name: str

    # 验证是否是正确时间格式字符串,不需要转化为datetime
    @field_validator('expires_time')
    def validate_expires_time(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError('expires_time must be in format %Y-%m-%d %H:%M:%S')
        return v
    # 验证是否是正确时间格式字符串,不需要转化为datetime
    @field_validator('refresh_expires_time')
    def validate_refresh_expires_time(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError('refresh_expires_time must be in format %Y-%m-%d %H:%M:%S')
        return v
    

    
class DouyinAuthResponse(BaseModel):
    status:str
    message:str
    data:DouyinOauthCredentials|None = None
