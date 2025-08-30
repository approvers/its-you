CONTAINER_NAME = its-you-app
IMAGE_NAME = its-you-developer

DEVELOPER_COMPOSE_FILE = compose.developer.yml
DEPLOY_COMPOSE_FILE = compose.deploy.yml

WORK_DIR_IN_CONTAINER = /opt/app

ruff:
	uv run ruff format
	uv run ruff check --fix

pytest:
	uv run pytest --cov=src --cov-report=html -v

mypy:
	uv run mypy . --strict

build:
	docker compose -f compose.developer.yml build

run:
	docker compose -f compose.developer.yml up -d

stop:
	docker compose -f compose.developer.yml down

check_running:
	@if docker ps -q -f name=$(CONTAINER_NAME) | grep -q .; then \
		echo "Container $(CONTAINER_NAME) is running"; \
	else \
		echo "Container $(CONTAINER_NAME) is not running"; \
	fi

exec:
	@if [ "$(filter-out $@,$(MAKECMDGOALS))" = "" ]; then \
		echo "Usage: make exec <command>"; \
		echo "Available commands: ruff, pytest, mypy"; \
		exit 1; \
	fi
	@if docker ps -q -f name=$(CONTAINER_NAME) | grep -q .; then \
		echo "Using running container $(CONTAINER_NAME)"; \
		docker exec $(CONTAINER_NAME) make $(filter-out $@,$(MAKECMDGOALS)); \
	elif docker images -q $(IMAGE_NAME) | grep -q .; then \
		echo "Using existing image $(IMAGE_NAME)"; \
		docker run --rm -v $(PWD):$(WORK_DIR_IN_CONTAINER) -w $(WORK_DIR_IN_CONTAINER) $(IMAGE_NAME) make $(filter-out $@,$(MAKECMDGOALS)); \
	else \
		echo "Building image..."; \
		make build; \
		docker run --rm -v $(PWD):$(WORK_DIR_IN_CONTAINER) -w $(WORK_DIR_IN_CONTAINER) $(IMAGE_NAME) make $(filter-out $@,$(MAKECMDGOALS)); \
	fi

%:
	@:
