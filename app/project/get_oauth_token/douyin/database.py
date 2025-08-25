from tk_db_utils import get_db_client
from .config import get_douyin_config
from .schemas import BaseTableEnhanced, OauthCredentialsTable
from sqlalchemy import select
from .models import DouyinOauthCredentials
from .logger import logger,logger_wrapper

class DouyinDbClient:
    _instance = None
    @logger_wrapper(level="INFO_DATABASE")
    def init_client(self):
        if self._instance is None:
            douyin_config = get_douyin_config()
            self._instance = get_db_client(env_file_path=douyin_config.env_path,
                                   db_config_path=douyin_config.config_path,
                                   database=BaseTableEnhanced)
        return self._instance

douyin_db_client = DouyinDbClient()

@logger_wrapper(level="INFO_DATABASE")
def update_douyin_oauth_credentials(oauth_credentials: DouyinOauthCredentials):
    db_client = douyin_db_client.init_client()
    try:
        with db_client.session_scope as session:
            stmt = select(OauthCredentialsTable).where(
                OauthCredentialsTable.controler_id == oauth_credentials.controler_id,
                OauthCredentialsTable.channel == 'douyin',
                )
            result = session.execute(stmt)
            if result.first():
                logger.info_database(f"get_douyin_oauth_token  controler_id:{oauth_credentials.controler_id} already exist")
                item = session.scalars(stmt).one()
                item.oauth_credentials = oauth_credentials.model_dump()
                db_operation_result = 'update'
                logger.info_database(f"controler_id:{oauth_credentials.controler_id},controler_name:{oauth_credentials.controler_name} is update")
            else:                
                oauth_credentials = OauthCredentialsTable(
                    controler_id=oauth_credentials.controler_id,
                    controler_name=oauth_credentials.controler_name,
                    channel="douyin",
                    oauth_credentials=oauth_credentials.model_dump(),
                )
                session.add(oauth_credentials)
                db_operation_result = 'insert'
                logger.info_database(f"controler_id:{oauth_credentials.controler_id},controler_name:{oauth_credentials.controler_name} is insert")
        return db_operation_result
    except Exception as e:
        logger.error_database(f"update_douyin_oauth_credentials error:{e}")
        return 'error'
