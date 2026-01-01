# app/models/flashcard.py
from sqlmodel import SQLModel, Field


class Flashcard(SQLModel, table=True):
    flashcard_id: int | None = Field(default=None, primary_key=True)
    flashcard_question: str
    flashcard_answer: str
    deck_id: int = Field(foreign_key="deck.id")
    knowledge_strength: str
    view_number: int
