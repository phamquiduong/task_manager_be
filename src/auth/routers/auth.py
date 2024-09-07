from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.orm import Session

from auth.constants.message import Message, UserMessage
from auth.constants.router import AuthRoutes
from auth.databases import check_database_connection
from auth.databases.dependency import get_session
from auth.exceptions import APIException
from auth.schemas.api.register import RegisterRequestSchema, RegisterResponseSchema
from auth.schemas.models.users import UserInSchema, UserOutSchema
from auth.schemas.response.error import Response400, Response409, Response422, Response500
from auth.services.user import UserService

auth_router = APIRouter(prefix=AuthRoutes.PREFIX, tags=["Authentication"])


@auth_router.get(
    path=AuthRoutes.Path.HEALTH_CHECK.path,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Response500},
    },
)
def health_check():
    check_database_connection()


@auth_router.post(
    path=AuthRoutes.Path.REGISTER.path,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": Response400},
        status.HTTP_409_CONFLICT: {"model": Response409},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": Response422},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Response500},
    },
)
def register(
    register_request: RegisterRequestSchema = Body(...),
    session: Session = Depends(get_session),
) -> RegisterResponseSchema:
    user_service = UserService(session=session)

    if user_service.is_exists_user_email(email=register_request.email):
        raise APIException(
            status_code=status.HTTP_409_CONFLICT,
            api_error_code=1,
            message=Message.RESPONSE_409,
            fields={"email": UserMessage.EMAIL_ALREADY_EXIST},
        )

    user_in = UserInSchema(email=register_request.email, password=register_request.password)

    user = user_service.create_user(user_in=user_in)

    user_out = UserOutSchema(**user.__dict__)

    return RegisterResponseSchema(data=user_out)
