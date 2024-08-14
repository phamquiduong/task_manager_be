from dotenv import load_dotenv

from auth.constants import ENV_FILE_DIR

if not load_dotenv(ENV_FILE_DIR):
    raise FileNotFoundError('Could not find environment variable')


def create_app():
    from fastapi import FastAPI

    from auth.router.auth import auth_router

    flask_app = FastAPI(
        title='Task Manager Auth Application',
        docs_url='/auth',
        openapi_url="/auth/openapi.json",
    )

    flask_app.include_router(auth_router)

    return flask_app


app = create_app()
