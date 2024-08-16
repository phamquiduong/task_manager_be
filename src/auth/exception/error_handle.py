from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

from auth.exception import APIException
from auth.schemas.base_response import FieldErrorSchema, ResponseFailBaseSchema


def handle_error(app: FastAPI) -> FastAPI:
    @app.exception_handler(HTTPException)
    async def http_exception_handler(_request: Request, http_exc: HTTPException):
        return JSONResponse(
            content=ResponseFailBaseSchema(status_code=http_exc.status_code, message=http_exc.detail).model_dump(),
            status_code=http_exc.status_code,
        )

    @app.exception_handler(APIException)
    async def api_exception_handler(_request: Request, api_exc: APIException):
        error_fields = (
            [FieldErrorSchema(name=name, message=msg) for name, msg in api_exc.fields.items()]
            if api_exc.fields
            else None
        )

        return JSONResponse(
            content=ResponseFailBaseSchema(
                status_code=api_exc.status_code, message=api_exc.message, fields=error_fields
            ).model_dump(),
            status_code=api_exc.status_code,
        )

    @app.exception_handler(Exception)
    async def exception_handler(_request: Request, exc: Exception):
        return JSONResponse(
            content=ResponseFailBaseSchema(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(exc)
            ).model_dump(),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return app
