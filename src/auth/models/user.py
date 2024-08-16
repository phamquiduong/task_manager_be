from typing import Callable

from sqlalchemy import BigInteger, Boolean, Column, DateTime, String, func

from auth.databases import Base

func: Callable


class UserModel(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    email = Column(String(255), unique=False, nullable=False, index=True)
    password = Column(String(255), nullable=True)

    full_name = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
