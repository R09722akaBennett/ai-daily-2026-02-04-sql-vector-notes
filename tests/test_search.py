from app.core.search import Note, tfidf_rank


def test_rank_returns_results() -> None:
    notes = [Note(1,'hello world'), Note(2,'hello tool')]
    out = tfidf_rank(notes, 'tool')
    assert out and out[0]['id'] == 2
