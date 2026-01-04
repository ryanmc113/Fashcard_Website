from pydantic import BaseModel, field_validator


class Flashcard(BaseModel):
    flashcard_id: int
    flashcard_question: str
    flashcard_answer: str
    deck_id: int
    knowledge_strength: str
    view_number: int

    @field_validator("flashcard_question", "flashcard_answer")
    @classmethod
    def not_blank(cls, v: str):
        if not v.strip():
            raise ValueError("Field cannot be blank")
        return v
