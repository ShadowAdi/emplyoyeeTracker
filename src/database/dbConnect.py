from sqlmodel import create_engine, SQLModel, Session
import os
from src.models import Company, Employee
from src.config import logger
from dotenv import load_dotenv
from datetime import datetime

now = datetime.now()

formatted_time = now.strftime("%H:%M:%S")

load_dotenv()
db_url = os.getenv("DB_URL")

if db_url is None:
    logger.error(f"Neon DB Url is not Exixt. Failed To Connect To DB {formatted_time}")
    raise ValueError(f"NEON_DB_URL environment variable is missing {formatted_time}")


engine = create_engine(db_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        logger.info(f"Session Has Been Closed {formatted_time}")
        session.close()
