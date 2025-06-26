from fastapi import FastAPI
from .database import create_db_and_tables
from dotenv import load_dotenv
load_dotenv()
create_db_and_tables()

app=FastAPI()


@app.get("/")
def read_root():
    return {
        "message":"Server Started",
        "success":True
    }

