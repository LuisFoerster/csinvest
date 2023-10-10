from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from settings import settings

engine = create_engine(settings.db_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
