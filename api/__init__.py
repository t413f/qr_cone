from fastapi import APIRouter
from .rotuters import router as r

router = APIRouter()

router.include_router(r)