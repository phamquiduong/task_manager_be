from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.orm import Session

from auth.constants.message import Message, UserMessage
from auth.databases.dependency import get_session
from auth.exceptions import APIException
from auth.schemas.api.register import RegisterRequestSchema, RegisterResponseSchema
from auth.schemas.models.users import UserInSchema, UserOutSchema
from auth.schemas.response.error import Response409, Response422, Response500
from auth.services.user import UserService

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.get("/health-check", status_code=status.HTTP_204_NO_CONTENT)
def health_check():
    pass


@auth_router.post(
    "/register",
    response_model=RegisterResponseSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {"model": Response409},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": Response422},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Response500},
    },
)
def register(
    register_request: RegisterRequestSchema = Body(...),
    session: Session = Depends(get_session),
):
    user_service = UserService(session=session)

    if user_service.is_exists_user_email(email=register_request.email):
        raise APIException(
            status_code=status.HTTP_409_CONFLICT,
            message=Message.RESPONSE_409,
            fields={"email": UserMessage.EMAIL_ALREADY_EXIST},
        )

    user_in = UserInSchema(email=register_request.email, password=register_request.password)

    user = user_service.create_user(user_in=user_in)
    session.commit()
    session.refresh(user)

    user_out = UserOutSchema(**user.__dict__)
    return RegisterResponseSchema(data=user_out)
