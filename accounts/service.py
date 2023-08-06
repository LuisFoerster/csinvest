import sqlalchemy as sa
from sqlalchemy.orm import Session

from accounts.models import Account


def create(*, db_session: Session, userid: int, account_in: dict):
    stmt = (
        sa.insert(Account)
        .values(userid=userid, **account_in)
    )
    db_session.execute(stmt)
    db_session.commit()
