from fastapi import APIRouter, Depends
from services import flashcard_service

router = APIRouter()


@router.get("/{deck_id}")
async def list_flashcards(deck_id):
    return ["party"]
