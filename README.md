# LC Data — Technical Exercise Environment

A small, self-contained environment for the round-2 session. It stands up a
Postgres + `pgvector` database and seeds it with a synthetic sample. Your
interviewers will share the exercises at the **start** of the session — you only
need the environment running beforehand.

## Before the session (please do this ~24h ahead)

**Prerequisites:** Docker (with `docker compose`) and Python 3.10+.

```bash
# 1. clone, then:
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. bring up the database (pgvector) and seed it
make up
make seed
```

`make seed` prints how many rows match a sample filter — if you see a line like
`Seeded 50000 rows. Rows matching UK+tax+in_force: 124 (0.248%)`, you're ready.

```bash
make psql     # optional: open a psql shell to poke around
make down     # stop + remove the database when you're done
```

The database is exposed on host port **55432** (not 5432, to avoid clashing with
a local Postgres). Override it by setting `HOST_DB_PORT` in `.env` if needed.

If anything fails to set up, tell us before the session so we sort it out — we
don't want to spend interview time on Docker.

## During the session

Your interviewer will walk you through **Task A** (`block_a/`) and **Task B**
(`block_b/`). Both are designed to be run, not just discussed — think out loud,
sketch if it helps, and you're welcome to write pseudocode instead of polished
code.

## Layout

```
docker-compose.yml   pgvector database
data/seed.py         seeds ~50k synthetic chunks + metadata + an HNSW index
block_a/             Task A — filtered vector search ("UK Tax" correctness)
block_b/             Task B — evaluating an embedding-model change
Makefile             shortcuts: up / seed / psql / blocka / gendata / down
```
