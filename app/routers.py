from fastapi import APIRouter

from app.schemas import Task, TaskCreate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks = [
    Task(
        id=1,
        title="Learn FastAPI",
        completed=False
    )
]


@router.get("/")
def get_tasks():
    return tasks


@router.post("/")
def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        completed=False
    )

    tasks.append(new_task)

    return new_task