from fastapi import FastAPI

from app_auth.router.auth import auth_router

app = FastAPI(
    title='Task Manager Auth Application',
    docs_url='/auth',
    openapi_url="/auth/openapi.json",
)

app.include_router(auth_router)
