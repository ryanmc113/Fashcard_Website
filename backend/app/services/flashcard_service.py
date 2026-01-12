from typing import List, Optional
from dal.flashcard_dal import FlashcardDAL
from models.db import flashcard as Flashcard
from schemas.flashcard import FlashcardSchema


class FlashcardService:
    def __init__(self, flashcard_dal: FlashcardDAL):
        self.flashcard_dal = flashcard_dal

    # add flashcard to a deck
    def add_flashcard_to_deck(self, flashcard: FlashcardSchema) -> Flashcard:
        flashcard = Flashcard()
        self.flashcard_dal.create(flashcard)
        return flashcard

    # use case: when you fell confident you know the answer
    # but don't want to delete it or see it for a bit
    def archive_flashcard(self, flashcard: Flashcard) -> Flashcard:
        pass

    def update_knowledge_strength(self, flashcard_id: int) -> bool:
        pass

    def remove_flashcard_from_deck(self, flashcard: Flashcard) -> bool:
        pass

    def flashcards_of_one_knowledge_strength():
        pass

    def flashcards_of_one_knowledge_strength_from_one_deck():
        pass
