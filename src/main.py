from fastapi import FastAPI
from .database import create_db_and_tables
from dotenv import load_dotenv
from .routes import CompanyRouter
import uvicorn

load_dotenv()
create_db_and_tables()

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Server Started", "success": True}


app.include_router(CompanyRouter.comapnyRouter)


if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)