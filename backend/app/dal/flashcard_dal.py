from sqlmodel import Session, select
from models.db.flashcard import FlashcardModel
from typing import List, Optional


class FlashcardDAL:
    def __init__(self, session: Session):
        self.session = session

    def create(self, flashcard: FlashcardModel) -> FlashcardModel:
        self.session.add(flashcard)
        self.session.commit()
        self.session.refresh(flashcard)
        return flashcard

    def get(self, flashcard_id: int) -> Optional[FlashcardModel]:
        statement = select(FlashcardModel).where(FlashcardModel.id == flashcard_id)
        result = self.session.exec(statement).first()
        return result

    def get_flashcards_by_deck(self, deck_id: int) -> List[FlashcardModel]:
        statement = select(FlashcardModel).where(FlashcardModel.deck_id == deck_id)
        result = self.session.exec(statement).all()
        return result
