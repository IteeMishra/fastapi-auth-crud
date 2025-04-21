from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from jose import JWTError,jwt

secret_key = os.getenv("secret_key")
algo=os.getenv("algo")

access_token_expiry_minutes=30

def create_access_token(data: dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=access_token_expiry_minutes)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,secret_key,algorithm=algo)

def to_decode(token:str):
    try:
        return jwt.decode(token,secret_key,algorithms=[algo])
    except JWTError:
        return None
    
