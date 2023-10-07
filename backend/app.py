from fastapi import FastAPI
from models import todo_list_pydantic, todo_list_pydantic_in, TodoList
from tortoise.contrib.fastapi import register_tortoise
import uvicorn

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = ['http://localhost:3000', "localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
async def root():
    return {'msg', 'hello world'}

@app.get('/todo')
async def view_groceries():
    response = await todo_list_pydantic.from_queryset(TodoList.all())
    return {"status": "ok", "data" : response}

@app.post('/todo')
async def add_item(supplier_info: todo_list_pydantic_in):
    todo_list = await TodoList.create(**supplier_info.dict(exclude_unset=True))
    response = await todo_list_pydantic.from_tortoise_orm(todo_list)
    return {"status": "ok", "data" : response}

@app.delete('/todo/')
async def delete_item(item_id: int):
    await TodoList.filter(id=item_id).delete()
    return {"status": "ok"}

@app.get('/todo/{item_id}')
async def toggle_item(item_id: int, completed: bool):
    item = await TodoList.get(id=item_id)
    item.completed = completed
    await item.save()
    response = await todo_list_pydantic.from_tortoise_orm(item)
    return {"status": "ok", "data": response}

register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models" : ["models"]},
    generate_schemas=True,
    add_exception_handlers=True 
)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)