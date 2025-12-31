from fastapi import APIRouter, Depends

# from app.dal.flashcard_dal import FlashcardDAL
from app.api.deps import get
from app.schemas.flashcard import Flas

router = APIRouter()
