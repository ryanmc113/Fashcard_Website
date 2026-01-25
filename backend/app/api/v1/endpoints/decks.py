from fastapi import APIRouter, Depends
from dal import deck_dal
from services.deck_service import DeckService
from schemas.deck import DeckSchema
from deps import get_deck_service

router = APIRouter()


@router.get("/")
async def list_decks():
    return ["deck party"]


@router.post("/create")
async def create_deck(payload: DeckSchema):
    service = DeckService(get_deck_service)
    return service.create_deck(payload)
