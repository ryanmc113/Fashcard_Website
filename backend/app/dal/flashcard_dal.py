from sqlmodel import Session
from app.models.db.flashcard import Flashcard


class FlashcardDAL:
    def __init__(self, session: Session):
        self.session = session

    def create(self, flashcard: Flashcard) -> Flashcard:
        self.session.add(Flashcard)
        self.session.commit()
        self.session.refresh(flashcard)
