from sqlmodel import create_engine, SQLModel, Session
import os
from src.models import Company, Employee
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DB_URL")

engine = create_engine(db_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
