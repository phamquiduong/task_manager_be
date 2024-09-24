from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from auth.constants.message import Message
from auth.constants.router import all_auth_router
from auth.exceptions import APIException
from auth.schemas.base_response import FieldErrorSchema, ResponseFailSchema
from auth.utils.error_handler import render_error_code


async def http_exception_handler(_request: Request, http_exc: HTTPException):
    raise APIException(status_code=http_exc.status_code, message=http_exc.detail)


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

    raise APIException(status_code=status.HTTP_400_BAD_REQUEST, message=Message.RESPONSE_400, fields=error_fields)


async def api_exception_handler(request: Request, api_exc: APIException):
    error_fields = (
        [FieldErrorSchema(name=name, message=msg) for name, msg in api_exc.fields.items()] if api_exc.fields else None
    )

    error_code = render_error_code(
        api_code=all_auth_router.get(request.scope["route"].path, 0),
        http_code=api_exc.status_code,
        api_code_detail=api_exc.api_error_code,
    )

    return JSONResponse(
        content=ResponseFailSchema(
            status_code=api_exc.status_code, message=api_exc.message, fields=error_fields, error_code=error_code
        ).model_dump(),
        status_code=api_exc.status_code,
    )


async def exception_handler(request: Request, exc: Exception):
    error_code = render_error_code(
        api_code=all_auth_router.get(request.scope["route"].path, 0),
        http_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        api_code_detail=0,
    )

    return JSONResponse(
        content=ResponseFailSchema(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(exc), error_code=error_code
        ).model_dump(exclude_none=True),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def handle_error(app: FastAPI):
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, request_validation_error_handler)
    app.add_exception_handler(APIException, api_exception_handler)
    app.add_exception_handler(Exception, exception_handler)
