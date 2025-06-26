from sqlmodel import create_engine, SQLModel
import os
from src.models import Company, Employee
from dotenv import load_dotenv
load_dotenv()
db_url = os.getenv("DB_URL")

engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
