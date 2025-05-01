from pydantic import BaseModel


class SearchRequest(BaseModel):
    """
    Pydantic model for search requests
    """
    search_text: str
