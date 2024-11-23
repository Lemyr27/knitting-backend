import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.settings import app_settings
from app.router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.CORS_ALLOW_ORIGINS,
    allow_credentials=app_settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=app_settings.CORS_ALLOW_METHODS,
    allow_headers=app_settings.CORS_ALLOW_HEADERS,
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
