from enum import StrEnum


class Message(StrEnum):
    RESPONSE_200 = "OK"

    RESPONSE_400 = "BAD_REQUEST"
    RESPONSE_409 = "CONFLICT"
    RESPONSE_422 = "UNPROCESSABLE_ENTITY"

    RESPONSE_500 = "INTERNAL_SERVER_ERROR"
