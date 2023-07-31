import sqlalchemy as sa
from sqlalchemy.orm import Session

from prices.models import Price

def create(*, db_session: Session, price_in) -> Price:
    db_session.bulk_insert_mappings(Price, price_in)
    db_session.commit()