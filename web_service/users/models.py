class UserBase(BaseModel):
    username: str
    role: str
    last_login: datetime = None
