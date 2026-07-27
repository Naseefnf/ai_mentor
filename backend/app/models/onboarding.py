from app.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class OnboardingProfile(Base):
    __tablename__ = "onboarding_profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    subject = Column(String, unique=False, nullable=False)
    skill_level = Column(String, nullable=False)
    goals = Column(String, nullable=False)
    learning_style = Column(String, nullable=False)
    feedback_style = Column(String, nullable=False)