from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String

from auth.databases import Base


class UserSession(Base):
    __tablename__ = 'user_sessions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    key = Column(String(255), unique=True, nullable=False, index=True)

    user_id = Column(BigInteger, ForeignKey(User.id), index=True)
    expired_at = Column(DateTime, nullable=False)
