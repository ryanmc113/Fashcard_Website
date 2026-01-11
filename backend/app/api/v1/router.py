from fastapi import APIRouter
from .endpoints import flashcards, decks

api_router = APIRouter()

api_router.include_router(
    flashcards.router,
    prefix="/flashcards",
    tags=["flashcards"],
)


api_router.include_router(
    decks.router,
    prefix="/decks",
    tags=["decks"],
)
