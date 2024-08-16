from typing import Any

from fastapi import status
from pydantic import BaseModel

from auth.constants.message import Message


class ResponseSucessBaseSchema(BaseModel):
    status_code: int = status.HTTP_200_OK
    message: str = Message.RESPONSE_200
    data: Any


class FieldErrorSchema(BaseModel):
    name: str
    message: str | list[str]

    def model_post_init(self, __context):
        if isinstance(self.message, str):
            self.message = [self.message]


class ResponseFailBaseSchema(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = Message.RESPONSE_400
    fields: list[FieldErrorSchema] | None = None
