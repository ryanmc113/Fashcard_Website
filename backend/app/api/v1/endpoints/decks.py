from fastapi import APIRouter, Depends
from dal import deck_dal
from services.deck_service import De

router = APIRouter()


@router.get("/")
async def list_decks():
    return ["deck party"]


@router.post("/create")
async def create_deck():
    return
