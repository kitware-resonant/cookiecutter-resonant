#!/bin/bash
set -exu

echo 'alias serve="uv run ./manage.py runserver 0.0.0.0:8000"' >> ~/.zshrc
