from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.onboarding import OnboardingProfile
from app.services.prompt_engine import generate_system_prompt

router = APIRouter(prefix="/prompt", tags=["prompt"])

@router.get("/me")
def get_my_prompt(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    profile = db.query(OnboardingProfile).filter(
        OnboardingProfile.user_id == current_user.id
    ).first()

    if profile is None:
        raise HTTPException(status_code=404, detail="Onboarding profile not found. Please complete onboarding first.")

    system_prompt = generate_system_prompt(profile)
    return {"system_prompt": system_prompt}