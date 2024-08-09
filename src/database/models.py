from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, String, func

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    email = Column(String(255), unique=False, nullable=False, index=True)
    password = Column(String(255), nullable=True)

    full_name = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


class UserSession(Base):
    __tablename__ = 'user_sessions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    key = Column(String(255), unique=True, nullable=False, index=True)

    user_id = Column(BigInteger, ForeignKey(User.id), index=True)
    expired_at = Column(DateTime, nullable=False)
