from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Backend Project")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Backend is running"}


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def get_tasks() -> list[Task]:
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate) -> Task:
    global next_task_id

    task = Task(
        id=next_task_id,
        title=task_data.title,
        description=task_data.description,
    )
    tasks.append(task)
    next_task_id += 1
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")
