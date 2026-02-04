from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.search import Note, tfidf_rank

router = APIRouter()

_NOTES = [
    Note(1, 'FastAPI + Streamlit in one repo'),
    Note(2, 'Tool schema versioning prevents drift'),
    Note(3, 'URL firewall reduces SSRF risk'),
]


class SearchRequest(BaseModel):
    query: str


@router.post('/notes/search')
def search(req: SearchRequest):
    return {'results': tfidf_rank(_NOTES, req.query)}
