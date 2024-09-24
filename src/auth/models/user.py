from sqlalchemy import BigInteger, Boolean, Column, String

from auth.databases import Base
from auth.models.base import TimestampMixin


class UserModel(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=True)

    full_name = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=False)
