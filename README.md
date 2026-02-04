# SQL + Vector Notes

FastAPI + Streamlit service demonstrating retrieval-style scoring.

## Why this project

Retrieval patterns power many agent products. This MVP shows a lightweight ranking approach with a small in-memory note store and a TF-IDF-like scorer.

## Inspiration / Sources

- TF-IDF — https://en.wikipedia.org/wiki/Tf%E2%80%93idf

## Architecture

- FastAPI backend: `app/` (app factory + routers + services + core domain)
- Streamlit UI: `app/web/streamlit_app.py`

## Run (dev)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
```

Terminal A (API):

```bash
API_PORT=8205 ./scripts/dev_api.sh
```

Terminal B (UI):

```bash
UI_API_URL=http://127.0.0.1:8205 streamlit run app/web/streamlit_app.py --server.port 8605
```

## Smoke test

```bash
curl -s http://127.0.0.1:8205/api/health | python3 -m json.tool
```

## Roadmap (Next steps)

- Add persistence (SQLite) where applicable
- Add auth + rate limiting
- Add background jobs + queue for long-running tasks
- Add Docker + deployment target
