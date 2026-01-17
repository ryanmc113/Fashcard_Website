from typing import List, Optional
from dal.deck_dal import DeckDAL
from models.db import deck as Deck
from schemas.deck import DeckSchema


class DeckService:
    def __init__(self, deck_dal: DeckDAL):
        self.deck_dal = deck_dal

    def create_deck(self, payload: DeckSchema) -> Deck:
        deck = Deck(
            name=payload.name,
            collection_id=payload.collection_id,
            tags=payload.tags,
            knowledge_strength=payload.knowledge_strength,
            view_number=payload.view_number,
        )

        return self.deck_dal.create(deck=deck)
