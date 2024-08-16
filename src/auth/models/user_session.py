from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String

from auth.databases import Base
from auth.models import UserModel


class UserSessionModel(Base):
    __tablename__ = "user_sessions"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    key = Column(String(255), unique=True, nullable=False, index=True)

    user_id = Column(BigInteger, ForeignKey(UserModel.id), index=True)
    expired_at = Column(DateTime, nullable=False)
