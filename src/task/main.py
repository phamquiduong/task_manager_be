from fastapi import FastAPI

app = FastAPI(
    title="Task Manager Application",
    docs_url="/manager",
    openapi_url="/manager/openapi",
)
