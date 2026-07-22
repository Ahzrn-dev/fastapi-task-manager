from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task,
    update_task,
)
router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
):
    return create_task(db, task)

@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task


@router.delete("/{task_id}", response_model=TaskResponse)
def remove_task(task_id: int, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task

@router.put("/{task_id}", response_model=TaskResponse)
def edit_task(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db),
):
    task = update_task(db, task_id, updated_task)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task