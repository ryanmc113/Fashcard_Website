from fastapi import APIRouter, Depends


router = APIRouter()


@router.get("/")
async def list_flashcards():
    return ["party"]
