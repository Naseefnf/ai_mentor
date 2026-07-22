from fastapi import FastAPI
from app.routers.health import router
from app.routers.auth import router as auth_router


app = FastAPI()

app.include_router(router)
app.include_router(auth_router)