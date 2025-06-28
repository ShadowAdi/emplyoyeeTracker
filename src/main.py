from fastapi import FastAPI
from .database import create_db_and_tables
from dotenv import load_dotenv
from .routes import CompanyRouter
from .middlewares import (
    validation_exception_handler,
    global_exception_handler,
    http_exception_handler,
    response_validation_error,
)
import uvicorn
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from .utils import add_cors

load_dotenv()
create_db_and_tables()

app = FastAPI()
add_cors(app=app)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ResponseValidationError, response_validation_error)


@app.get("/")
def read_root():
    return {"message": "Server Started", "success": True}


app.include_router(CompanyRouter.comapnyRouter)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
