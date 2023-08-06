import sqlalchemy as sa
from sqlalchemy.orm import Session

from accounts.models import Account


def create(*, db_session: Session, account):
    stmt = (
        sa.insert(Account).
        values(account)
    )
    db_session.execute(stmt)
    db_session.commit()


