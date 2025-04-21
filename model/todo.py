from pydantic import BaseModel,EmailStr

class Todo(BaseModel):
    name:str
    description : str
    complete:bool
    

class User(BaseModel):
    user_name:str
    email:EmailStr
    password:str

class Login(BaseModel):
    email:EmailStr
    password:str