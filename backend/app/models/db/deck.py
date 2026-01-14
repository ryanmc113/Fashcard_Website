# app/models/deck.py
from sqlmodel import SQLModel, Field


class Deck(SQLModel, table=True):
    __tablename__ = "deck"
    deck_id: int | None = Field(default=None, primary_key=True)
    name: str
    collection_id: int = Field(foreign_key="collection.collection_id")
    knowledge_strength: str = "new"
    view_number: int = 0
