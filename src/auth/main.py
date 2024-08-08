from fastapi import FastAPI

app = FastAPI(
    docs_url='/auth',
    openapi_url="/auth/openapi.json"
)
