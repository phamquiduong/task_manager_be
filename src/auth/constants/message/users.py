from enum import StrEnum


class UserMessage(StrEnum):
    CREATE_USER_SUCCESS = "Create user successfully"
    PASSWORD_REGEX_NOT_MATCH = "Password must contain at least one letter, one digit, and one special character"
    USER_WITH_EMAIL_ALREADY_EXIST = "User with email already exists"
