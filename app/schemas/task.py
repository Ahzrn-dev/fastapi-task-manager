from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str


class TaskCreate(TaskBase):
    pass
class TaskUpdate(BaseModel):
    title: str
    completed: bool


class TaskResponse(TaskBase):
    id: int
    completed: bool

    model_config = {
        "from_attributes": True
    }