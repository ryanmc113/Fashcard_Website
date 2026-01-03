from app.db.session import get_session
from app.dal.flashcard_dal import FlashcardDAL
from fastapi import Depends


def get_flascard_dal(session=Depends(get_session)):
    return FlashcardDAL(session)
