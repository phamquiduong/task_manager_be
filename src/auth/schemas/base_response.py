from typing import Any

from fastapi import status
from pydantic import BaseModel

from auth.constants.message import Message


class ResponseBaseSchema(BaseModel):
    status_code: int
    message: str


class ResponseSucessBaseSchema(ResponseBaseSchema):
    status_code: int = status.HTTP_200_OK
    message: str = Message.RESPONSE_200
    data: Any


class ResponseFailBaseSchema(ResponseBaseSchema):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = Message.RESPONSE_400
    error_code: str = "ERR-000-000-000"


class FieldErrorSchema(BaseModel):
    name: str
    message: str | list[str]

    def model_post_init(self, __context):
        if isinstance(self.message, str):
            self.message = [self.message]


class ResponseFailSchema(ResponseFailBaseSchema):
    fields: list[FieldErrorSchema] | None = None
