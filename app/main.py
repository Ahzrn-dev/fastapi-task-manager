from fastapi import FastAPI

from app.api.tasks import router as task_router
from app.core.database import Base, engine

app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(task_router)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Task Manager API is running",
    }