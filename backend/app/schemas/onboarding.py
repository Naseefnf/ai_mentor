from pydantic import BaseModel

class OnboardingCreate(BaseModel):
    subject: str
    skill_level: str
    goals: str
    learning_style: str
    feedback_style: str

class OnboardingResponse(BaseModel):
    id: int
    user_id: int
    subject: str
    skill_level: str
    goals: str
    learning_style: str
    feedback_style: str

    class Config:
            from_attributes = True