from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

app = FastAPI()

tasks: List[Task] = [
    Task(id=1, title="Task 1", description="Description 1", status="not completed"),
    Task(id=2, title="Task 2", description="Description 2", status="completed"),
]

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    if next((t for t in tasks if t.id == task.id), None):
        raise HTTPException(status_code=400, detail="Task with this ID already exists")
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task)
    return {"detail": "Task deleted"}
