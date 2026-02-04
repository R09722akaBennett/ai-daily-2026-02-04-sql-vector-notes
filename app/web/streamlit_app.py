from __future__ import annotations

import os

import httpx
import streamlit as st

API_URL = os.getenv('UI_API_URL', 'http://127.0.0.1:8000')

st.set_page_config(page_title='SQL + Vector Notes', layout='centered')
st.title('SQL + Vector Notes')
st.caption('MVP retrieval-style search with a tiny TF-IDF scorer (no external deps).')

q = st.text_input('Query', value='tool schema')
if st.button('Search'):
    with httpx.Client(base_url=API_URL, timeout=10.0) as client:
        r = client.post('/api/notes/search', json={'query': q})
        st.json(r.json())
