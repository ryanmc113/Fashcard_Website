from sqlmodel import Session, select
from app.models.db.flashcard import Flashcard
from typing import List, Optional


class FlashcardDAL:
    def __init__(self, session: Session):
        self.session = session

    def create(self, flashcard: Flashcard) -> Flashcard:
        self.session.add(flashcard)
        self.session.commit()
        self.session.refresh(flashcard)
        return flashcard

    def get(self, flashcard_id: int) -> Optional[Flashcard]:
        statement = select(Flashcard).where(Flashcard.id == flashcard_id)
        result = self.session.exec(statement).first()
        return result

    def get_flashcards_by_deck(self, deck_id: int) -> List[Flashcard]:
        statement = select(Flashcard).where(Flashcard.deck_id == deck_id)
        result = self.session.exec(statement).all()
        return result
