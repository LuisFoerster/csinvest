import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy.orm import Session, joinedload
from asset_stacks.models import AssetStack


def create(*, db_session: Session, asset_stack_in):
    stmt = (
        sa.insert(AssetStack).
        values(asset_stack_in)
    )
    db_session.add(stmt)
    db_session.commit()


