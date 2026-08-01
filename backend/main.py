from fastapi import FastAPI
from app.routers.health import router
from app.routers.auth import router as auth_router
from app.routers.onboarding import router as onboarding_router
from app.routers.prompt import router as prompt_router



app = FastAPI()

app.include_router(router)
app.include_router(auth_router)
app.include_router(onboarding_router)
app.include_router(prompt_router)
