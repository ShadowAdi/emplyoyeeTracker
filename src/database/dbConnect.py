from sqlmodel import create_engine, SQLModel
import os
from models import Company, Employee

db_url = os.getenv("DB_URL")

engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
