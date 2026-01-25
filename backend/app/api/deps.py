from db.session import get_session
from dal.flashcard_dal import FlashcardDAL
from fastapi import Depends
from dal.deck_dal import DeckDAL
from services.deck_service import DeckService


def get_flascard_dal(session=Depends(get_session)):
    return FlashcardDAL(session)


def get_deck_dal(session=Depends(get_session)):
    return DeckDAL(session)


def get_deck_service(deck_dal: DeckDAL = Depends(get_deck_dal)) -> DeckService:
    return DeckService(deck_dal)
