from pydantic import BaseModel, Field

class StudentBase(BaseModel):
    name: str = Field(description="Student full name")
    age: int = Field(ge=16, le=100)
    group_id: int


class StudentCreate(StudentBase):
    pass


class StudentGet(StudentBase):
    id: int