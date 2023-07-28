from pydantic import BaseModel
from sqlalchemy import Column, String, Text, Integer, Boolean

from database.base import Base

"""SQL-Alchemy Model"""


class User(Base):
    __tablename__ = "users"
    steamid = Column(String(64), primary_key=True)
    personaname = Column(Text)
    personastateflags = Column(Integer)
    profileurl = Column(Text)
    avatar = Column(Text)
    avatarhash = Column(Text)
    avatarmedium = Column(Text)
    avatarfull = Column(Text)
    personastate = Column(Integer)
    communityvisibilitystate = Column(Integer)
    profilestate = Column(Integer)
    lastlogoff = Column(Integer)
    commentpermission = Column(Boolean)

    # Private Data (May not be available for all users)
    realname = Column(Text, default=None)
    primaryclanid = Column(Text, default=None)
    timecreated = Column(Integer, default=None)
    gameid = Column(Integer, default=None)
    gameserverip = Column(Integer, default=None)
    gameextrainfo = Column(Text, default=None)
    cityid = Column(Integer, default=None)
    loccountrycode = Column(Text, default=None)
    locstatecode = Column(Text, default=None)
    loccityid = Column(Integer, default=None)


"""Pydantic Model"""


class UserBase(BaseModel):
    steamid: str
    personaname: str
    personastateflags: int
    profileurl: str
    avatar: str
    avatarhash: str
    avatarmedium: str
    avatarfull: str
    personastate: int
    communityvisibilitystate: int
    profilestate: int
    lastlogoff: int
    commentpermission: int
    realname: str = None
    primaryclanid: str = None
    timecreated: int = None
    gameid: int = None
    gameserverip: str = None
    gameextrainfo: str = None
    cityid: int = None
    loccountrycode: str = None
    locstatecode: str = None
    loccityid: int = None

    class Config:
        from_attributes = True
