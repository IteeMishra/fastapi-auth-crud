from fastapi import FastAPI
from routes.route import router as todo_router
from routes.index_route import router as index_router
from routes.user import router as user_route
app=FastAPI()


app.include_router(index_router,tags=["index"])
app.include_router(todo_router,tags=["Todos"],prefix="/todo")
app.include_router(user_route, tags=["User"])