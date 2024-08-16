import re

from fastapi import status
from pydantic import BaseModel, EmailStr, Field, field_validator

from auth.constants.message import UserMessage
from auth.constants.regex import USER_PASSWORD_REGEX
from auth.schemas.base_response import ResponseSucessBaseSchema
from auth.schemas.models.users import UserOutSchema


class RegisterRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str):
        if not re.match(USER_PASSWORD_REGEX, password):
            raise ValueError(UserMessage.PASSWORD_REGEX_NOT_MATCH)
        return password


class RegisterResponseSchema(ResponseSucessBaseSchema):
    status_code: int = status.HTTP_201_CREATED
    message: str = UserMessage.CREATE_USER_SUCCESS
    data: UserOutSchema
