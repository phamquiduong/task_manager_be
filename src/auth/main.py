from dotenv import load_dotenv

from auth.constants import ENV_FILE_DIR

if not load_dotenv(ENV_FILE_DIR):
    raise FileNotFoundError("Could not find environment variable")


def create_app():
    # pylint: disable=C0415
    from fastapi import FastAPI

    from auth.exceptions.error_handle import handle_error
    from auth.routers.auth import auth_router

    fastapi_app = FastAPI(
        title="Task Manager Auth Application",
        docs_url="/auth",
        openapi_url="/auth/openapi.json",
    )

    fastapi_app.include_router(auth_router)

    return handle_error(fastapi_app)


app = create_app()
