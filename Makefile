.PHONY: up down seed psql blocka gendata clean

up:
	docker compose up -d
	@echo "Waiting for Postgres to be healthy..."
	@until docker compose exec -T db pg_isready -U lc -d lc >/dev/null 2>&1; do sleep 1; done
	@echo "Database is up on localhost:$${HOST_DB_PORT:-55432} (user lc / db lc)."

down:
	docker compose down -v

seed:
	python data/seed.py

psql:
	docker compose exec db psql -U lc -d lc

blocka:
	python block_a/filtered_search.py

gendata:
	python block_b/make_data.py

clean: down
