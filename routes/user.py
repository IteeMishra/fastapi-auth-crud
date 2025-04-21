from fastapi import APIRouter,HTTPException,status
from Authentication.token import create_access_token
from model.todo import User,Login
from config.database import collection_user
from Authentication.auth import hashing_password,verify_password
router=APIRouter()

@router.post("/register_user")
async def create_user(user:User):
    hashed_pwd=hashing_password(user.password)
    user_dict={"name":user.user_name,"email":user.email,"password":hashed_pwd}

    collection_user.insert_one(user_dict)
    return {"user registered successfully"}



@router.post("/login")
async def login(user:Login):
    db_user=collection_user.find_one({"email":user.email})
    if not db_user or not verify_password(user.password,db_user["password"]):
        raise HTTPException(status_code=400,detail="Invalid Credentials")
    
    token =create_access_token(data={"user_id":str(db_user["_id"])})
    return {"access_token":token,"token_type":"bearer"}



