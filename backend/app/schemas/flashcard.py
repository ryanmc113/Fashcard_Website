from pydantic import BaseModel, field_validator


class FlashcardSchema(BaseModel):
    id: int
    flashcard_question: str
    flashcard_answer: str
    deck_id: int
    knowledge_strength: str
    view_number: int

    @field_validator("flashcard_question", "flashcard_answer")
    @classmethod
    def not_blank(cls, field: str):
        if not field.strip():
            raise ValueError("f{field} cannot be blank")
        return field
