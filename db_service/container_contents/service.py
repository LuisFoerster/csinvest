import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as postgres_sa
from sqlalchemy import func
from sqlalchemy.orm import Session

from db_service.container_contents.schema import ContainerContent


def create(*, db_session: Session, relation_in):
    stmt = sa.insert(ContainerContent).values(relation_in)
    db_session.execute(stmt)
    db_session.commit()


def upsert(*, db_session: Session, relation_in: list[dict]):
    stmt = (
        postgres_sa.insert(ContainerContent)
        .values(relation_in)
        .on_conflict_do_update(
            constraint='unique_relation',
            #index_elements=['id'],
            set_={
                "updated_at": func.current_timestamp()
            }
        ))
    db_session.execute(stmt)
    db_session.commit()
