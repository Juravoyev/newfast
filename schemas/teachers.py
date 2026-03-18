from pydantic import BaseModel, Field

class TeacherBase(BaseModel):
    name: str = Field(description="Teacher full name")
    subject: str = Field(description="Subject name")


class TeacherCreate(TeacherBase):
    pass


class TeacherGet(TeacherBase):
    id: int