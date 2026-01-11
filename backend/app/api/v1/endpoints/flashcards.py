from fastapi import APIRouter, Depends
from dal import flashcard_dal

router = APIRouter()


@router.get("/{deck_id}")
async def list_flashcards(deck_id):
    return flashcard_dal.get(deck_id)
