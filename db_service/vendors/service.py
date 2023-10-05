import sqlalchemy as sa
from sqlalchemy.orm import Session

from db_service import Vendor


def create(*, db_session: Session, vendor_in):
    stmt = sa.insert(Vendor).values(vendor_in)
    db_session.execute(stmt)
    db_session.commit()
