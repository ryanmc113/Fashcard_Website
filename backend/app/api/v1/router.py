from fastapi import APIRouter
from .endpoints import flashcards

api_router = APIRouter()

api_router.include_router(
    flashcards.router,
    prefix="/flashcards",
    tags=["flashcards"],
)
