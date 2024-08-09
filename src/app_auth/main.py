from fastapi import FastAPI

app = FastAPI(
    title='Task Manager Auth Application',
    docs_url='/auth',
    openapi_url="/auth/openapi.json"
)
