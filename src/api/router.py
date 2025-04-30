from fastapi import APIRouter

from src.api.schemas import SearchRequest

router = APIRouter()


@router.post("/search")
async def search_request(request: SearchRequest):
    pass
