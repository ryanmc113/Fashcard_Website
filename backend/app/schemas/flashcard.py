from pydantic import BaseModel


class Flashcard(BaseModel):
    flashcard_id: int
    # front
    flashcard_question: str
    # back
    flashcard_answer: str
    deck_id: int
    knowledge_strength: str
    view_number: int
