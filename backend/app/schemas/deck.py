from pydantic import BaseModel


class Deck(BaseModel):
    deck_id: int
    name: str
    collection_id: int
    tags: str
    view_number: int
