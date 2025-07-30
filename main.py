from app.log import create_logger, reload_logger_level
from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.project.get_oauth_token import oauth_router

logger = create_logger(__name__)

app = FastAPI(
    title="hnzzzsw api2",
    description="api后台系统",
    version="1.0.0",
)


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred."},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

app.include_router(oauth_router)

@app.get("/")
async def read_root():
    logger.info('测试日志记录是否正常')
    return {"message": "API2  is running."}

@app.get("/reload")
async def reload():
    reload_logger_level(logger)
    return {"message": "日志级别已重载"}
    
