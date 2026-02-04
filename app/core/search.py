from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Note:
    id: int
    text: str


def tfidf_rank(notes: list[Note], query: str) -> list[dict]:
    # tiny TF-IDF-ish scorer (no deps)
    q = [t.lower() for t in query.split() if t.strip()]
    if not q:
        return []

    def score(note: Note) -> float:
        words = [t.lower() for t in note.text.split()]
        s = 0.0
        for term in q:
            tf = words.count(term) / max(1, len(words))
            df = sum(1 for n in notes if term in n.text.lower())
            idf = math.log((1 + len(notes)) / (1 + df)) + 1
            s += tf * idf
        return s

    ranked = sorted(((n, score(n)) for n in notes), key=lambda t: t[1], reverse=True)
    return [{'id': n.id, 'score': float(s), 'text': n.text} for n,s in ranked[:5]]
