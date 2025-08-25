[2025-08-25 16:50:56 +0800] [494240] [INFO] Starting gunicorn 23.0.0
[2025-08-25 16:50:56 +0800] [494240] [INFO] Listening at: http://0.0.0.0:40024 (494240)
[2025-08-25 16:50:56 +0800] [494240] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2025-08-25 16:50:56 +0800] [494241] [INFO] Booting worker with pid: 494241
[2025-08-25 16:50:56 +0800] [494242] [INFO] Booting worker with pid: 494242
[2025-08-25 16:50:56 +0800] [494243] [INFO] Booting worker with pid: 494243
[2025-08-25 16:50:56 +0800] [494244] [INFO] Booting worker with pid: 494244
[2025-08-25 16:50:58 +0800] [494242] [ERROR] Exception in worker process
Traceback (most recent call last):
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 608, in spawn_worker
worker.init_process()
~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/uvicorn/workers.py", line 75, in init_process
super().init_process()
~~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 135, in init_process
self.load_wsgi()
~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 147, in load_wsgi
self.wsgi = self.app.wsgi()
~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 66, in wsgi
self.callable = self.load()
~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
return self.load_wsgiapp()
~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
return util.import_app(self.app_uri)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/util.py", line 370, in import_app
mod = importlib.import_module(module)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/importlib/__init__.py", line 88, in import_module
return _bootstrap._gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
File "/www/wwwroot/api2_hnzzzsw/main.py", line 6, in <module>
from app.project.get_oauth_token import oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/__init__.py", line 3, in <module>
from .douyin import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/__init__.py", line 1, in <module>
from .service import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/service.py", line 2, in <module>
from .database import update_douyin_oauth_credentials
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/database.py", line 3, in <module>
from .schemas import BaseTableEnhanced,OauthCredentialsTable
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/schemas.py", line 19, in <module>
class OauthCredentialsTable(BaseTableEnhanced):
...<11 lines>...
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_api.py", line 845, in __init_subclass__
_as_declarative(cls._sa_registry, cls, cls.__dict__)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 245, in _as_declarative
return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 326, in setup_mapping
return _ClassScanMapperConfig(
registry, cls_, dict_, table, mapper_kw
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 577, in __init__
self._setup_table(table)
~~~~~~~~~~~~~~~~~^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 1762, in _setup_table
table_cls(
~~~~~~~~~^
tablename,
^^^^^^^^^^
...<3 lines>...
**table_kw,
^^^^^^^^^^^
),
^
File "<string>", line 2, in __new__
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
return fn(*args, **kwargs) # type: ignore[no-any-return]
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 429, in __new__
return cls._new(*args, **kw)
~~~~~~~~^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 461, in _new
raise exc.InvalidRequestError(
...<5 lines>...
)
sqlalchemy.exc.InvalidRequestError: Table 'oauth_db.oauth_credentials' is already defined for this MetaData instance. Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
[2025-08-25 16:50:58 +0800] [494241] [ERROR] Exception in worker process
Traceback (most recent call last):
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 608, in spawn_worker
worker.init_process()
~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/uvicorn/workers.py", line 75, in init_process
super().init_process()
~~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 135, in init_process
self.load_wsgi()
~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 147, in load_wsgi
self.wsgi = self.app.wsgi()
~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 66, in wsgi
self.callable = self.load()
~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
return self.load_wsgiapp()
~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
return util.import_app(self.app_uri)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/util.py", line 370, in import_app
mod = importlib.import_module(module)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/importlib/__init__.py", line 88, in import_module
return _bootstrap._gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
File "/www/wwwroot/api2_hnzzzsw/main.py", line 6, in <module>
from app.project.get_oauth_token import oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/__init__.py", line 3, in <module>
from .douyin import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/__init__.py", line 1, in <module>
from .service import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/service.py", line 2, in <module>
from .database import update_douyin_oauth_credentials
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/database.py", line 3, in <module>
from .schemas import BaseTableEnhanced,OauthCredentialsTable
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/schemas.py", line 19, in <module>
class OauthCredentialsTable(BaseTableEnhanced):
...<11 lines>...
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_api.py", line 845, in __init_subclass__
_as_declarative(cls._sa_registry, cls, cls.__dict__)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 245, in _as_declarative
return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 326, in setup_mapping
return _ClassScanMapperConfig(
registry, cls_, dict_, table, mapper_kw
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 577, in __init__
self._setup_table(table)
~~~~~~~~~~~~~~~~~^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 1762, in _setup_table
table_cls(
~~~~~~~~~^
tablename,
^^^^^^^^^^
...<3 lines>...
**table_kw,
^^^^^^^^^^^
),
^
File "<string>", line 2, in __new__
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
return fn(*args, **kwargs) # type: ignore[no-any-return]
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 429, in __new__
return cls._new(*args, **kw)
~~~~~~~~^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 461, in _new
raise exc.InvalidRequestError(
...<5 lines>...
)
sqlalchemy.exc.InvalidRequestError: Table 'oauth_db.oauth_credentials' is already defined for this MetaData instance. Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
[2025-08-25 16:50:58 +0800] [494244] [ERROR] Exception in worker process
Traceback (most recent call last):
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 608, in spawn_worker
worker.init_process()
~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/uvicorn/workers.py", line 75, in init_process
super().init_process()
~~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 135, in init_process
self.load_wsgi()
~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 147, in load_wsgi
self.wsgi = self.app.wsgi()
~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 66, in wsgi
self.callable = self.load()
~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
return self.load_wsgiapp()
~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
return util.import_app(self.app_uri)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/util.py", line 370, in import_app
mod = importlib.import_module(module)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/importlib/__init__.py", line 88, in import_module
return _bootstrap._gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
File "/www/wwwroot/api2_hnzzzsw/main.py", line 6, in <module>
from app.project.get_oauth_token import oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/__init__.py", line 3, in <module>
from .douyin import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/__init__.py", line 1, in <module>
from .service import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/service.py", line 2, in <module>
from .database import update_douyin_oauth_credentials
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/database.py", line 3, in <module>
from .schemas import BaseTableEnhanced,OauthCredentialsTable
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/schemas.py", line 19, in <module>
class OauthCredentialsTable(BaseTableEnhanced):
...<11 lines>...
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_api.py", line 845, in __init_subclass__
_as_declarative(cls._sa_registry, cls, cls.__dict__)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 245, in _as_declarative
return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 326, in setup_mapping
return _ClassScanMapperConfig(
registry, cls_, dict_, table, mapper_kw
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 577, in __init__
self._setup_table(table)
~~~~~~~~~~~~~~~~~^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 1762, in _setup_table
table_cls(
~~~~~~~~~^
tablename,
^^^^^^^^^^
...<3 lines>...
**table_kw,
^^^^^^^^^^^
),
^
File "<string>", line 2, in __new__
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
return fn(*args, **kwargs) # type: ignore[no-any-return]
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 429, in __new__
return cls._new(*args, **kw)
~~~~~~~~^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 461, in _new
raise exc.InvalidRequestError(
...<5 lines>...
)
sqlalchemy.exc.InvalidRequestError: Table 'oauth_db.oauth_credentials' is already defined for this MetaData instance. Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
[2025-08-25 16:50:58 +0800] [494244] [INFO] Worker exiting (pid: 494244)
[2025-08-25 16:50:58 +0800] [494242] [INFO] Worker exiting (pid: 494242)
[2025-08-25 16:50:58 +0800] [494241] [INFO] Worker exiting (pid: 494241)
[2025-08-25 16:50:58 +0800] [494243] [ERROR] Exception in worker process
Traceback (most recent call last):
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 608, in spawn_worker
worker.init_process()
~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/uvicorn/workers.py", line 75, in init_process
super().init_process()
~~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 135, in init_process
self.load_wsgi()
~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/workers/base.py", line 147, in load_wsgi
self.wsgi = self.app.wsgi()
~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 66, in wsgi
self.callable = self.load()
~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
return self.load_wsgiapp()
~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
return util.import_app(self.app_uri)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/util.py", line 370, in import_app
mod = importlib.import_module(module)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/importlib/__init__.py", line 88, in import_module
return _bootstrap._gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
File "/www/wwwroot/api2_hnzzzsw/main.py", line 6, in <module>
from app.project.get_oauth_token import oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/__init__.py", line 3, in <module>
from .douyin import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/__init__.py", line 1, in <module>
from .service import douyin_oauth_router
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/service.py", line 2, in <module>
from .database import update_douyin_oauth_credentials
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/database.py", line 3, in <module>
from .schemas import BaseTableEnhanced,OauthCredentialsTable
File "/www/wwwroot/api2_hnzzzsw/app/project/get_oauth_token/douyin/schemas.py", line 19, in <module>
class OauthCredentialsTable(BaseTableEnhanced):
...<11 lines>...
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_api.py", line 845, in __init_subclass__
_as_declarative(cls._sa_registry, cls, cls.__dict__)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 245, in _as_declarative
return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 326, in setup_mapping
return _ClassScanMapperConfig(
registry, cls_, dict_, table, mapper_kw
)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 577, in __init__
self._setup_table(table)
~~~~~~~~~~~~~~~~~^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/orm/decl_base.py", line 1762, in _setup_table
table_cls(
~~~~~~~~~^
tablename,
^^^^^^^^^^
...<3 lines>...
**table_kw,
^^^^^^^^^^^
),
^
File "<string>", line 2, in __new__
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
return fn(*args, **kwargs) # type: ignore[no-any-return]
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 429, in __new__
return cls._new(*args, **kw)
~~~~~~~~^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/sqlalchemy/sql/schema.py", line 461, in _new
raise exc.InvalidRequestError(
...<5 lines>...
)
sqlalchemy.exc.InvalidRequestError: Table 'oauth_db.oauth_credentials' is already defined for this MetaData instance. Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
[2025-08-25 16:50:58 +0800] [494243] [INFO] Worker exiting (pid: 494243)
[2025-08-25 16:50:58 +0800] [494240] [ERROR] Worker (pid:494244) exited with code 3
[2025-08-25 16:50:58 +0800] [494240] [ERROR] Worker (pid:494241) was sent SIGTERM!
[2025-08-25 16:50:58 +0800] [494240] [ERROR] Worker (pid:494242) exited with code 3
Traceback (most recent call last):
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 208, in run
self.sleep()
~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 359, in sleep
ready = select.select([self.PIPE[0]], [], [], 1.0)
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 241, in handle_chld
self.reap_workers()
~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 529, in reap_workers
raise HaltServer(reason, self.WORKER_BOOT_ERROR)
gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/bin/gunicorn", line 8, in <module>
sys.exit(run())
~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 66, in run
WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]", prog=prog).run()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 235, in run
super().run()
~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 71, in run
Arbiter(self).run()
~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 228, in run
self.halt(reason=inst.reason, exit_status=inst.exit_status)
~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 341, in halt
self.stop()
~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 395, in stop
time.sleep(0.1)
~~~~~~~~~~^^^^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 241, in handle_chld
self.reap_workers()
~~~~~~~~~~~~~~~~~^^
File "/www/server/pyporject_evn/api2_hnzzzsw_venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 529, in reap_workers
raise HaltServer(reason, self.WORKER_BOOT_ERROR)
gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>
