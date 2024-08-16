from enum import StrEnum


class Message(StrEnum):
    RESPONSE_200 = "OK"
    RESPONSE_400 = "Bad Request"
    RESPONSE_500 = "Internal Server Error"
