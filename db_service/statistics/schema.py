from sqlalchemy import Column,  text, Float, DateTime, func, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db_service.base import Base


class Statistic(Base):
    __tablename__ = "statistics"
    id = Column(Integer, autoincrement=True, primary_key=True)
    classid = Column(ForeignKey("items.classid"))
    return_of_investment = Column(Float)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="statistic")

