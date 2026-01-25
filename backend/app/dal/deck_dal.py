from sqlmodel import Session, select
from models.db.deck import DeckModel
from typing import List, Optional


class DeckDAL:
    def __init__(self, session: Session):
        self.session = session

    def create(self, deck: DeckModel) -> DeckModel:
        self.session.add(deck)
        self.session.commit()
        self.session.refresh(deck)
        return deck

    # def get()
