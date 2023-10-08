from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    role: str
    last_login: datetime = None
