import sqlalchemy as sa
from sqlalchemy.orm import Session

from buyin_stacks.models import BuyinStack


def create(*, db_session: Session, buyin_stack_in):
    stmt = (
        sa.insert(BuyinStack).
        values(buyin_stack_in)
    )
    db_session.add(stmt)
    db_session.commit()

def create_or_update(*, db_session: Session, buyin_stack_in):
    stmt = (
        sa.insert(BuyinStack)
        .values(buyin_stack_in)
    )

    update_stmt = stmt.on_duplicate_key_update(

    )

    db_session.execute(update_stmt)
    db_session.commit()


