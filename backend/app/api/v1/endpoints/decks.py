from fastapi import APIRouter, Depends
from dal import deck_dal
from services.deck_service import DeckService
from schemas.deck import DeckSchema

router = APIRouter()


@router.get("/")
async def list_decks():
    return ["deck party"]


@router.post("/create")
async def create_deck(payload: DeckSchema):
    return DeckService.create_deck(payload)
