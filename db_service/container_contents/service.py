import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy.orm import Session
from sqlalchemy import func
from db_service.container_contents.schema import ContainerContent


def create(*, db_session: Session, relation_in):
    stmt = sa.insert(ContainerContent).values(relation_in)
    db_session.execute(stmt)
    db_session.commit()


def create_or_skip(*, db_session: Session, relation_in: list[dict]):
    stmt = (
        mysql_sa.insert(ContainerContent)
        .values(relation_in)
        .on_duplicate_key_update(updated_at=func.current_timestamp())
    )
    try:
        db_session.execute(stmt)
        db_session.commit()
    except:
        print("error catched in create or skip")