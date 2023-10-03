import sqlalchemy
from sqlalchemy.orm import Session

from db_service.users.schema import User


def get(*, db_session: Session, steamid: str) -> User:
    stmt = sqlalchemy.select(User).where(User.steamid == steamid)
    return db_session.execute(stmt).scalar()


def create(*, db_session: Session, user_in: dict) -> None:
    stmt = sqlalchemy.insert(User).values(**user_in)
    db_session.execute(stmt)
    db_session.commit()
