from sqlalchemy.orm import Session

from auth.models import UserModel
from auth.schemas.models.users import UserInSchema, UserOutSchema


class UserService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_user(self, user_in: UserInSchema) -> UserOutSchema:
        user = UserModel(**user_in.model_dump())

        self.session.add(user)
        self.session.flush([user])

        return UserOutSchema(**user.__dict__)

    def is_exists_user_email(self, email: str) -> bool:
        return self.session.query(UserModel).filter(UserModel.email == email).first() is not None
