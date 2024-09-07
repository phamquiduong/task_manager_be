from fastapi import status

from auth.constants.message import Message


class APIException(Exception):
    def __init__(
        self,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        api_error_code: int = 0,
        message: str = Message.RESPONSE_400,
        fields: dict[str, str | list[str]] | None = None,
    ) -> None:
        self.status_code = status_code
        self.api_error_code = api_error_code
        self.message = message
        self.fields = fields
