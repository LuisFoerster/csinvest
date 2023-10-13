from sqlalchemy import Column, text, Integer, DateTime, func, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import TIMESTAMP

from db_service.base import Base


class ContainerContent(Base):
    __tablename__ = "container_contents"
    id = Column(Integer, autoincrement=True, primary_key=True)
    container_classid = Column(ForeignKey("items.classid"))
    content_classid = Column(ForeignKey("items.classid"))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    __table_args__ = (
        UniqueConstraint('container_classid', 'content_classid', name='unique_relation'),
    )
