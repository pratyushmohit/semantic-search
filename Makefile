ifneq (,$(wildcard ./.env))
    include .env
    export
endif

install:
	poetry install --with=dev

fastapi-endpoint-local:
	python -m uvicorn semantic_search.main:app --reload --host=0.0.0.0 --port=8000

build-fastapi:
	docker build -t semantic-search -f docker\fastapi\Dockerfile .

build-celery:
	docker build -t celery-worker -f docker\celery\Dockerfile .

run:
	docker run -dp 0.0.0.0:8000:8000 semantic-search

up-dev:
	docker-compose up -d

down-dev:
	docker-compose down

qdrant_up:
	docker run -it -d -p 6333:6333 \
		-v qdrant_storage:/qdrant/storage \
		qdrant/qdrant