from dotenv import load_dotenv
from tk_db_utils import init_db
import os

load_dotenv()


class Test(object):
    def __init__(self):
        self.host: Optional[str] = os.getenv("DB_HOST")
        self.port: str = os.getenv("DB_PORT", "3306")
        self.username: str = os.getenv("DB_USERNAME", "root")
        self.password: str = os.getenv("DB_PASSWORD", "password")
        init_db()
        
    def print_info(self):
        print(self.host)
        print(self.port)
        print(self.username)
        print(self.password)


if __name__ == "__main__":
    test = Test()
    test.print_info()
