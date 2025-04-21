from fastapi import APIRouter

router=APIRouter()

@router.get('/')
def index():
    return {"this is a simple app with only backend and database as of now, you can perform CRUD in here!"}
