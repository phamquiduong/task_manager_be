from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr
    full_name: str


class UserOutSchema(UserBaseSchema):
    id: int
    is_active: bool


class UserInSchema(UserBaseSchema):
    full_name: str | None = None
    password: str

    def model_post_init(self, __context):
        if not self.full_name:
            self.full_name = self.email.rsplit("@", 1)[0]
