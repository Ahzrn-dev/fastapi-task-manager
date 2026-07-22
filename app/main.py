from fastapi import FastAPI

from app.routers import router

app = FastAPI(
    title="Task Manager API",
    description="A RESTful Task Management API built with FastAPI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Welcome to Task Manager API"}


app.include_router(router)