from pydantic import BaseModel, Field

class SubmissionBase(BaseModel):
    exam_id: int
    student_id: int
    student_answer: str = Field(description="Student answer")


class SubmissionCreate(SubmissionBase):
    pass


class SubmissionGet(SubmissionBase):
    id: int
    score: float = Field(ge=0, le=100)
    feedback: str