from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.onboarding import OnboardingProfile
from app.schemas.onboarding import OnboardingCreate, OnboardingResponse

router = APIRouter(prefix="/onboarding", tags=["onboarding"])

@router.post("/", response_model=OnboardingResponse)
def submit_onboarding(
    data: OnboardingCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    new_profile = OnboardingProfile(
        user_id=current_user.id,
        subject=data.subject,
        skill_level=data.skill_level,
        goals=data.goals,
        learning_style=data.learning_style,
        feedback_style=data.feedback_style,
    )
    db.add(new_profile)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Onboarding profile already exists for this user")

    db.refresh(new_profile)
    return new_profile