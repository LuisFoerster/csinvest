import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy.orm import Session, joinedload
from accounts.models import Account


def create(*, db_session: Session, account):
    stmt = (
        sa.insert(Account).
        values(account)
    )
    db_session.add(stmt)
    db_session.commit()


