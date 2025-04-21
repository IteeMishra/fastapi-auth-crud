from fastapi import APIRouter,HTTPException,status,Depends,Header
from Authentication.token import to_decode
from model.todo import Todo
from config.database import collection_name
from schema.schemas import list_serial,individual_serial
from bson import ObjectId

router=APIRouter()

#getting current user - authenciated user will only be authorized to access certain endpoints
def get_current_user(token:str=Header(...)):
    payload=to_decode(token)
    print(payload)
    if not payload:
        raise HTTPException(status_code=404,detail="Unauthorized")
    return payload["user_id"]


#getting all todos
@router.get('/')
async def get_todos(user_id:str=Depends(get_current_user)):
    todos= list_serial(collection_name.find())
    
    return todos

#getting specific todo as per the id
@router.get('/{id}')
def get_specific_todo(id: str,user_id:str=Depends(get_current_user)):
    todo=individual_serial(collection_name.find_one({"_id":ObjectId(id)}))
    return todo

#creating a todo
@router.post('/')
async def createe_todo(todo:Todo,user_id:str=Depends(get_current_user)):
    collection_name.insert_one(dict(todo))


#creating an update API
@router.put('/{id}')
def put_todo(id:str,todo:Todo,user_id:str=Depends(get_current_user)):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})
    return f"Item with id = {id} has been updated."

#creating a delete API
@router.delete("/{id}")
async def delete_todo(id:str,user_id:str=Depends(get_current_user)):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    return {f"Item with id = {id} has been deleted."}



