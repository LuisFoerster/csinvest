import sqlalchemy as sa
from sqlalchemy.orm import Session

from accounts.models import Account


def create(*, db_session: Session, account_in: dict):
    stmt = (
        sa.insert(Account)
        .values( **account_in)
    )
    db_session.execute(stmt)
    db_session.commit()

def exists(*, db_session: Session, steamid:str):
    stmt = (
        sa.select(Account)
        .where(Account.steamid == steamid)
    )
    result = db_session.execute(stmt).scalar()
    return result