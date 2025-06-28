from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt, ExpiredSignatureError
from dotenv import load_dotenv
from src.config import logger
from src.config import CustomAuthError
import os


load_dotenv()

HASH_SECRET = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2scheme = OAuth2PasswordBearer(tokenUrl="/company/login")


def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, algorithm=ALGORITHM, HASH_SECRET=HASH_SECRET)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, HASH_SECRET, ALGORITHM)
        return payload
    except ExpiredSignatureError:
        logger.error("Token Is Expired")
        raise CustomAuthError("Token Is Expired. Try To Login Again")
    except JWTError as e:
        logger.error(f"Got Error In Decoding Token {str(e)}")
        raise CustomAuthError("Invalid token. Try To Login Again")
