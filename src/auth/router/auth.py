from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.orm import Session

from auth.constants.message import UserMessage
from auth.databases.dependency import get_session
from auth.exception import APIException
from auth.schemas.api.register import RegisterRequestSchema, RegisterResponseSchema
from auth.schemas.models.users import UserInSchema, UserOutSchema
from auth.services.user import UserService

auth_router = APIRouter(prefix="/auth")


@auth_router.get("/health-check")
def health_check():
    return {}


@auth_router.post("/register", response_model=RegisterResponseSchema, status_code=status.HTTP_201_CREATED)
def register(
    register_request: RegisterRequestSchema = Body(...),
    session: Session = Depends(get_session),
):
    user_service = UserService(session=session)

    if user_service.is_exists_user_email(email=register_request.email):
        raise APIException(
            status_code=status.HTTP_409_CONFLICT,
            message=UserMessage.USER_ALREADY_EXIST,
            fields={"email": UserMessage.EMAIL_ALREADY_EXIST},
        )

    user_in = UserInSchema(email=register_request.email, password=register_request.password)

    user = user_service.create_user(user_in=user_in)
    session.commit()
    session.refresh(user)

    user_out = UserOutSchema(**user.__dict__)
    return RegisterResponseSchema(data=user_out)
