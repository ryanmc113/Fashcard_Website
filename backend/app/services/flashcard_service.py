from typing import List, Optional
from dal import flashcard_dal as Flashcard_dal
from models.db import flashcard


class FlashcardService:
    def __init__(self, flashcard_dal: Flashcard_dal):
        self.flashcard_dal = flashcard_dal
