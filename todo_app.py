from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="To-Do App", description="A simple To-Do app API", version="1.0.0")

# In-memory database for storing To-Do items
todo_items = []

# Pydantic model for To-Do items
class TodoItem(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

@app.post("/todos/", response_model=TodoItem, status_code=201)
def add_todo_item(todo: TodoItem):
    # Check if the ID already exists
    if any(item["id"] == todo.id for item in todo_items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    todo_items.append(todo.dict())
    return todo

@app.get("/todos/", response_model=List[TodoItem])
def list_todo_items():
    return todo_items

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, updated_todo: TodoItem):
    for index, item in enumerate(todo_items):
        if item["id"] == todo_id:
            todo_items[index] = updated_todo.dict()
            return updated_todo
    raise HTTPException(status_code=404, detail="Item not found.")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo_item(todo_id: int):
    for index, item in enumerate(todo_items):
        if item["id"] == todo_id:
            del todo_items[index]
            return
    raise HTTPException(status_code=404, detail="Item not found.")