from fastapi import APIRouter, Depends
from services.flashcard_service import FlashcardService
from schemas.flashcard import FlashcardSchema

router = APIRouter()


@router.get("/{deck_id}")
async def list_flashcards(deck_id: int):
    return ["party"]


@router.post("/flashcard")
async def add_flashcard_to_deck(payload: FlashcardSchema):
    return FlashcardService.add_flashcard_to_deck(payload)
