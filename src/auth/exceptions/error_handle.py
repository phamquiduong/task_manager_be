from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from auth.constants.message import Message
from auth.exceptions import APIException
from auth.schemas.base_response import FieldErrorSchema, ResponseFailSchema


def handle_error(app: FastAPI) -> FastAPI:
    @app.exception_handler(HTTPException)
    async def http_exception_handler(_request: Request, http_exc: HTTPException):
        return JSONResponse(
            content=ResponseFailSchema(status_code=http_exc.status_code, message=http_exc.detail).model_dump(),
            status_code=http_exc.status_code,
        )

    @app.exception_handler(RequestValidationError)
    async def request_validation_error_handler(_request: Request, request_validation_error: RequestValidationError):
        error_fields = {}

        for pydantic_error in request_validation_error.errors():
            loc, msg = pydantic_error["loc"], pydantic_error["msg"]

            msg = msg.replace("Value error, ", "")
            msg = msg.capitalize()

            loc = [
                field_name
                for field_name in loc
                if field_name not in ("body", "query", "path") and isinstance(field_name, str)
            ] or ("__all__",)

            for field in loc:
                error_fields[field] = msg

        raise APIException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, message=Message.RESPONSE_422, fields=error_fields
        )

    @app.exception_handler(APIException)
    async def api_exception_handler(_request: Request, api_exc: APIException):
        error_fields = (
            [FieldErrorSchema(name=name, message=msg) for name, msg in api_exc.fields.items()]
            if api_exc.fields
            else None
        )

        return JSONResponse(
            content=ResponseFailSchema(
                status_code=api_exc.status_code, message=api_exc.message, fields=error_fields
            ).model_dump(),
            status_code=api_exc.status_code,
        )

    @app.exception_handler(Exception)
    async def exception_handler(_request: Request, exc: Exception):
        return JSONResponse(
            content=ResponseFailSchema(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(exc)
            ).model_dump(),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return app
