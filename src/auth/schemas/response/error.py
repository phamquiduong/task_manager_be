from fastapi import status

from auth.constants.message import Message
from auth.schemas.base_response import ResponseFailBaseSchema, ResponseFailSchema


class Response409(ResponseFailSchema):
    status_code: int = status.HTTP_409_CONFLICT
    message: str = Message.RESPONSE_409


class Response422(ResponseFailSchema):
    status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY
    message: str = Message.RESPONSE_422


class Response500(ResponseFailBaseSchema):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = Message.RESPONSE_500
