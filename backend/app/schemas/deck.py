from pydantic import BaseModel, field_validator


class DeckSchema(BaseModel):
    deck_id: int
    name: str
    collection_id: int
    tags: str
    knowledge_strength: str
    view_number: int


@field_validator("name")
@classmethod
def not_blank(cls, field: str):
    if not field.strip():
        raise ValueError("Name cannot be blank")
