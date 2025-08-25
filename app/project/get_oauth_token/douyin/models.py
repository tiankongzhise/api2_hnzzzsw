from pydantic import BaseModel
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
    expires_time: datetime
    refresh_token: str
    refresh_expires_time: datetime
    controler_id: str
    controler_name: str

class DouyinAuthResponse(BaseModel):
    status:str
    message:str
    data:DouyinOauthCredentials|None = None
