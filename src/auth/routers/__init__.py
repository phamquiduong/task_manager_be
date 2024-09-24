from fastapi import FastAPI


def include_route(app: FastAPI):
    # pylint: disable=C0415
    from auth.routers.auth import auth_router

    app.include_router(auth_router)
