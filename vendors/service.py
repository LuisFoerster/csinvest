import sqlalchemy as sa
from sqlalchemy.orm import Session

from vendors.models import Vendor


def create(*, db_session: Session, vendor_in):
    stmt = sa.insert(Vendor).values(vendor_in)
    db_session.execute(stmt)
    db_session.commit()
