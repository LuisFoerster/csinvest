from datetime import datetime

from sqlalchemy import Column, String, Text, text, func, DateTime, Integer
from pydantic import BaseModel

from db_service.migrations import Base

"""SQL-Alchemy Model"""


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text, unique=True)
    role = Column(String(32))
    last_login = Column(DateTime)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    #account = relationship("Account", back_populates="user", cascade="all, delete-orphan")


"""Pydantic Model"""


