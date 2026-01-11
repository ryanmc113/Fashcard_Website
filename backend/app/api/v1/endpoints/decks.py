from fastapi import APIRouter, Depends
from dal import deck_dal

router = APIRouter()


@router.get("/")
async def list_decks():
    return ["deck party"]
