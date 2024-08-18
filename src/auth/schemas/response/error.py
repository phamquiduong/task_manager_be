from fastapi import status

from auth.schemas.base_response import ResponseFailBaseSchema, ResponseFailSchema


class Response409(ResponseFailSchema):
    status_code: int = status.HTTP_409_CONFLICT
    message: str = "CONFLICT"


class Response422(ResponseFailSchema):
    status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY
    message: str = "UNPROCESSABLE_ENTITY"


class Response500(ResponseFailBaseSchema):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = "INTERNAL_SERVER_ERROR"
