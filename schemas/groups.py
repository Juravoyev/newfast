from pydantic import BaseModel, Field

class GroupBase(BaseModel):
    name: str = Field(description="Group name")
    modul: int = Field(ge=1, le=10)


class GroupCreate(GroupBase):
    pass


class GroupGet(GroupBase):
    id: int
