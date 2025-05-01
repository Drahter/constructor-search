from fastapi import APIRouter, HTTPException
from sqlalchemy import select, String

from src.api.database import new_session
from src.api.schemas import SearchRequest

router = APIRouter()


@router.post("/search")
async def universal_search(search_request: SearchRequest) -> list:
    """
    Gets JSON file with search_text parameter
    Searches for matches in database
    Returns list of matched objects with all parameters in JSON
    --------
    Before use change ... for model for search.
    """
    async with new_session() as session:
        query = select(...)
        for column in ....__table__.columns:
            if isinstance(column.type, String):
                query = query.where(getattr(..., column.name).ilike(f"%{search_request.search_text}%"))

        result = await session.execute(query)
        matches = result.scalars().all()

        if not matches:
            raise HTTPException(status_code=404, detail="Matches not found")

        return matches

