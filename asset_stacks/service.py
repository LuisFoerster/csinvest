import sqlalchemy as sa
from sqlalchemy.orm import Session

from asset_stacks.models import AssetStack


def create(*, db_session: Session, asset_stack_in):
    stmt = (
        sa.insert(AssetStack).
        values(asset_stack_in)
        .returning(AssetStack.id)
    )
    result = db_session.execute(stmt)
    db_session.commit()
    return result.scalar()



def create_or_update(*, db_session: Session, asset_stack_in):
    stmt = (
        sa.insert(AssetStack)
        .values(asset_stack_in)
    )

    update_stmt = stmt.on_duplicate_key_update(

    )

    db_session.execute(update_stmt)
    db_session.commit()

def get_all(*, db_session: Session, steamid: str):
    stmt = (
        sa.select(AssetStack)
        .where(AssetStack.steamid == steamid)
    )
    result = db_session.execute(stmt).scalars().all()
    return result

def get(*, db_session: Session, steamid: str, classid:str):
    stmt = (
        sa.select(AssetStack)
        .where(AssetStack.steamid == steamid)
        .where(AssetStack.classid == classid)
    )
    result = db_session.execute(stmt).scalar()
    return result

def get_id_by_classid_and_buyin(*, db_session: Session, steamid:str, classid:str, buyin:float):
    stmt = (
        sa.select(AssetStack)
        .where(AssetStack.steamid == steamid)
        .where(AssetStack.classid == classid)
        .where(AssetStack.buyin == buyin)
    )
    result = db_session.execute(stmt).scalar()
    return result

