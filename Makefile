# PWD = Print Working Directory - текущая рабочая директория
IMAGE_NAME=typing-homework

build:
	docker build -t $(IMAGE_NAME) .

typing:
	docker run --rm -v $(PWD):/app $(IMAGE_NAME) mypy /app/src
