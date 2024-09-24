from fastapi import FastAPI

from auth.exceptions.error_handle import handle_error
from auth.routers import include_route
from auth.utils.load_env import load_env_from_file

app = FastAPI(
    title="Task Manager Authentication Application",
    docs_url="/auth",
    openapi_url="/auth/openapi",
)

load_env_from_file()

handle_error(app)

include_route(app)
