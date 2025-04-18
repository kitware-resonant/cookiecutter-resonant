FROM python:3.13-slim

# Install system librarires for Python packages.
RUN apt-get update && \
    && apt-get install --no-install-recommends --yes \
        watchman \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Docker Compose will also mount this at runtime.
RUN --mount=source=.,target=/opt/django-project \
    pip install --no-cache-dir --editable /opt/django-project[dev]

# Use a directory name which will never be an import name, as isort considers this as first-party.
WORKDIR /opt/django-project
